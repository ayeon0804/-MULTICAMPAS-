from flask import Flask, render_template, redirect, request, url_for
from db import WorldCityDB

app = Flask(__name__)

@app.route('/')
def index():
    db = WorldCityDB()
    country_list = db.get_country_list()
    db.db_free()
    return render_template('index.html', country_list=country_list, totalCount=len(country_list))

@app.route('/search_list', methods=['GET'])
def search_list():
    db = WorldCityDB()
    country_name = request.args['country_name']
    country_list = db.search_country_list(country_name)
    db.db_free()
    return render_template('index.html', country_list=country_list, totalCount=len(country_list))

@app.route('/country_add')
def country_add():
    return render_template('country_add.html')

@app.route('/country_add_commit', methods=['POST'])
def country_add_commit():
    Code = request.form.get('Code')
    Name = request.form.get('Name')
    GNP = request.form.get('GNP')
    Population = request.form.get('Population')

    db = WorldCityDB()
    db.country_add(Code, Name, GNP, Population)
    db.db_free()
    return redirect(url_for('index'))

@app.route('/country/<no>')
def country(no):
    db = WorldCityDB()
    result = db.get_country_no(no)
    db.db_free()
    return render_template('country.html', country=result)

@app.route('/country_delete/<no>')
def country_delete(no):
    db = WorldCityDB()
    result = db.get_country_no(no)
    db.db_free()
    return render_template('country_delete.html', country=result)

@app.route('/country_delete_commit/<no>')
def country_delete_commit(no):
    db = WorldCityDB()
    db.country_delete(no)
    db.db_free()
    return redirect('index')

@app.route('/country_update/<no>')
def country_update(no):
    db = WorldCityDB()
    result = db.get_country_no(no)
    db.db_free()
    return render_template('country_update.html', country=result)

@app.route('/country_update_commit', methods=['POST'])
def country_update_commit():
    db = WorldCityDB()

    GNP = request.form['GNP']
    Population = request.form['Population']
    No = request.form['No']

    db.country_update(GNP, Population, No)
    db.db_free()
    return redirect(url_for('country', no=int(No)))


if __name__ == '__main__':
    app.run(debug=True)