import numpy as np
from flask import Flask, request, render_template
import pickle

app = Flask(__name__)
model = pickle.load(open('knn.pkl', 'rb'))


@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    features = [int(x) for x in request.form.values()]
    final_feaures = [np.array(features)]
    predict = model.predict(final_feaures)
    target_names = ['setosa', 'versicolor', 'virginica']
    output= target_names[predict[0]]
    print(output)
    return render_template('index.html', predict_text='Your IRIS is:{}'.format(output))

if __name__ == "__main__":
    app.run(debug=True)