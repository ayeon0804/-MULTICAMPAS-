from flask import Flask

app = Flask(__name__)

@app.route('/') 
def index():
    return 'Welcome Page'

@app.route('/<name>') 
def puppylatin(name):
    if str(name).find('-'):
        return str(name).replace('-',' ')
    else : return name

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=1234, debug=True)
