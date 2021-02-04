import io
from flask import Flask, render_template, Response, request
import matplotlib.pyplot as plt
import matplotlib
from matplotlib.backends.backend_agg import FigureCanvasAgg
import random

app = Flask(__name__)

@app.route('/')
def index():
    num_x = int(request.args.get('num_x', 50))
    return render_template('index.html', num_x = num_x)

@app.route('/matplot-imag.png')
def plot_png():
    fig = plt.figure()
    axis = fig.add_subplot(1,1,1)
    x = range(45)
    y = [random.randint(1,30) for ele in x]
    axis.plot(x, y)
    output = io.BytesIO()
    FigureCanvasAgg(fig).print_png(output)
    return Response(output.getvalue(), mimetype='image/png')

@app.route('/matplot-imag-<int:num_x>.png')
def plot_png2(num_x):
    fig = plt.figure()
    axis = fig.add_subplot(1,1,1)
    x = range(num_x)
    y = [random.randint(1,30) for ele in x]
    axis.plot(x, y)
    output = io.BytesIO()
    FigureCanvasAgg(fig).print_png(output)
    return Response(output.getvalue(), mimetype='image/png')


'''
# fig = matplotlib.Figure()
x = range(45)
y = [random.randint(1,30) for ele in x]
# matplot-imag.png
plt.plot(x, y)
# plt.show()
'''

if __name__ == '__main__':
    app.run(debug=True)