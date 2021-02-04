from flask import Flask, request, flash, url_for, redirect, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:1234@localhost:3306/pythondb'
app.config['SECRET_KEY'] = 'random string'

db = SQLAlchemy(app)

class students(db.Model):
    id = db.Column('id', db.Integer, primary_key=True)
    name = db.Column(db.String(10))
    city = db.Column(db.String(50))
    addr = db.Column(db.String(200))
    pin = db.Column(db.String(10))

    def __init__(self, name, city, addr, pin):
        self.name = name
        self.city = city
        self.addr = addr
        self.pin = pin

@app.route('/')
def index():
    return render_template('index.html', students=students.query.all())

@app.route('/new', methods=['GET','POST'])
def new():
    if request.method == 'POST':
        student = students(request.form['name'], request.form['city'], request.form['addr'], request.form['pin'])
        db.session.add(student)
        db.session.commit()
        return redirect(url_for('index'))
    return render_template('new.html')

if __name__ == '__main__':
    app.run(debug=True)