from flask import Flask, render_template, make_response, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/setcookie', methods=['POST','GET'])
def setCookie():
    if request.method == 'POST':
        user = request.form['nm']
    
    response = make_response(render_template('readcookie.html'))
    response.set_cookie('USER_ID', user)
    return response

@app.route('/getcookie')
def getCookie():
    name = request.cookies.get('USER_ID')
    if name != None:
        print(name)
        return '<h1>Welcome ' + name + '</h1>'
    else:
        return "I can't get cookie"

if __name__ == '__main__':
    app.run(debug=True)