from flask import Flask, request

app = Flask(__name__)

@app.route('/')
def hello():
    return 'Hello Flask'

@app.route('/search/')
def search():
    first = request.args.get('first')
    second = request.args.get('second')
    print(first, second)
    return '<h1>first:{0} second:{1}</h1>'.format(first, second)

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=1234, debug=True)