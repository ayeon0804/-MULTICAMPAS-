from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('5_Home.html')

@app.route('/robot/<name>')
def robot(name):
    return render_template('5_robot.html', name=name)

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=1234, debug=True)