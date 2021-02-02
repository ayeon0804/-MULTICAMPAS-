from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('1_request_arg.html')

@app.route('/result', methods=['POST','GET'])
def result():
    if request.method == 'POST':
        data1 = request.form['data1']
        data2 = request.form.get('data1')
        data3 = request.form.get('data2')
    else:
        data1 = request.args['data1']
        data2 = request.args.get('data1')
        data3 = request.values.get('data2')
    return 'data1 : %s , data2 : %s , data3 : %s' %(data1, data2, data3)

if __name__ == '__main__':
    app.run(debug=True)
