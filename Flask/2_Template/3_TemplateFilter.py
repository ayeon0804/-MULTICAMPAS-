from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def index():
    return '<h1>Goto/robot/name</h1>'

@app.route('/robot/<name>')
def robot_name(name):
    return render_template('3_TemplateFilter.html', name=name)

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=1234, debug=True)