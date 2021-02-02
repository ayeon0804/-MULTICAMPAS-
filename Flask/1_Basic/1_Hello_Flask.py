from flask import Flask

app = Flask(__name__)

@app.route('/hello')
def index():
    return 'Hello Flask'

@app.route('/bye')
def index2():
    return '<h1>bye Flask</h1>'

if __name__ == '__main__':
    app.run()