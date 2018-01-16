from flask import Flask
app = Flask(__name__)


def hello_world():
    return 'Hello, World!'

if __name__ == '__main__':
    from wsgiref.simple_server import make_server

    httpd = make_server('localhost', 5555, hello_world)
    httpd.serve_forever()
