from flask import Flask

app = Flask('__name__')

def index():
    return 'Hello Flask'

def about():
    return 'This is about page'

app.add_url_rule('/', '', index)
app.add_url_rule('/about', 'about', about)

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=1234, debug=True)