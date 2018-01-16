

def wsgi_app(environ, start_response):

    from flask import render_template
    return render_template('index.html')

if __name__ == '__main__':
    wsgi_app.run()
