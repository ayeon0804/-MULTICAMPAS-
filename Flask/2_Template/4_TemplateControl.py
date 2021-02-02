from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def index():
    robots = ['Cyber','King','Star']
    return render_template('4_TemplateControl.html', robots=robots)

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=1234, debug=True)