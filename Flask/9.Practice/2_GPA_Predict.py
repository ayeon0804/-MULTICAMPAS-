from flask import Flask, render_template, request
import pickle

app = Flask(__name__)
model = pickle.load(open('model.pkl', 'rb'))

@app.route('/')
def index():
    return render_template('2_GPA_Predict.html')

@app.route('/predict', methods=['POST'])
def predict():
    if request.method == 'POST':
        sat = int(request.form['sat'])
        pred = model.predict([sat])
        return render_template('2_GPA_Predict.html', gpa_score='GPA : {0}'.format(pred))

if __name__ == '__main__':
    app.run(debug=True)