from flask import Flask

app = Flask(__name__)

@app.route('/hello')
def hello():
    return 'Hello Flask'

@app.route('/bye')
def bye():
    return '<h1>bye Flask</h1>'

@app.route('/model/<name>')
def model(name):
    return '<h1>This is a page for {}</h1>'.format(name)

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=1234, debug=True)