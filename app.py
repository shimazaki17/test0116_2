

def wsgi_app(environ, start_response):

    from flask import render_template
    return render_template('index.html')

if __name__ == '__main__':
    from wsgiref.simple_server import make_server

    httpd = make_server('localhost', 5555, wsgi_app)
    httpd.serve_forever()
