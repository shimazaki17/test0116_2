
def hello_world():
    status = '200 OK'
    response_headers = [('Content-type', 'text/plain')]
    start_response(status, response_headers)

    response_body = 'Hello World'
    yield response_body.encode()

from wsgiref.simple_server import make_server
httpd = make_server('localhost', 5555, hello_world)
httpd.serve_forever()
