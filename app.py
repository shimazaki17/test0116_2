
def hello_world():
    status = '200 OK'
    response_headers = [('Content-type', 'text/plain')]
    start_response(status, response_headers)

    return [b"Hello World"]

if __name__ == '__main__':
    from wsgiref.simple_server import make_server
    httpd = make_server('localhost', 5555, hello_world)
    print("Serving on port 8000...")
    httpd.serve_forever()
