import sys
from wsgiref.simple_server import make_server

def not_found(env):
    request_path = env['PATH_INFO']

    status = '404 Not Found'
    headers = [('Content-Type', 'text/plain; charset=utf-8')]
    body = 'Not Found: {}'.format(request_path)

    return status, headers, body

def bad_request(env):
    request_method = env['REQUEST_METHOD']
    request_path = env['PATH_INFO']

    status = '400 Bad Request'
    headers = [('Content-Type', 'text/plain; charset=utf-8')]
    body = 'Bad Request: {} {}'.format(request_method, request_path)

    return status, headers, body

def index(env):
    status = '200 OK'
    headers = [('Content-Type', 'text/plain; charset=utf-8')]
    body = 'Hello, world!'

    return status, headers, body

def cat(env):
    status = '200 OK'
    headers = [('Content-Type', 'text/plain; charset=utf-8')]
    body = 'にゃーん'

    return status, headers, body

def routing(env):
    request_method = env['REQUEST_METHOD']
    request_path = env['PATH_INFO']

    allowed_request_method = {'GET', 'POST'}

    router = {
        'GET': {
            '/': index,
            '/cat': cat,
        },
        'POST': {
        }
    }

    if request_method not in allowed_request_method:
        return bad_request(env)

    return router[request_method].get(request_path, not_found)(env)

def app(env, start_response):
    status, headers, body_raw = routing(env)
    body = [bytes(line, encoding='utf-8') for line in body_raw.splitlines()]

    start_response(status, headers)
    return body

def main(argv):
    httpd = make_server('localhost', 8080, app)
    httpd.serve_forever()

    return 0

if __name__ == '__main__':
    sys.exit(main(sys.argv))
