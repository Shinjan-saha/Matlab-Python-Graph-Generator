from flask import Flask, render_template, request
import numpy as np
import matplotlib.pyplot as plt
from io import BytesIO
import base64

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/plot', methods=['POST'])
def plot():
    # Get input data from the user and split by comma
    voltage_red = np.array(list(map(float, request.form.get('voltage_red').split(','))))
    current_red = np.array(list(map(float, request.form.get('current_red').split(','))))
    voltage_blue = np.array(list(map(float, request.form.get('voltage_blue').split(','))))
    current_blue = np.array(list(map(float, request.form.get('current_blue').split(','))))
    voltage_green = np.array(list(map(float, request.form.get('voltage_green').split(','))))
    current_green = np.array(list(map(float, request.form.get('current_green').split(','))))

    # Create the plot
    plt.figure(figsize=(10, 6))
    plt.plot(voltage_red, current_red, color='red', label='Red Curve(2V)')
    plt.plot(voltage_blue, current_blue, color='blue', label='Blue Curve(6V)')
    plt.plot(voltage_green, current_green, color='green', label='Green Curve(10V)')

    # Add labels and title
    plt.xlabel('Base Emitter Voltage (V)')
    plt.ylabel('Base Current (μA)')
    plt.title('Current vs Voltage')
    plt.legend()

    # Save the plot to a BytesIO object
    plot_img = BytesIO()
    plt.savefig(plot_img, format='png')
    plot_img.seek(0)

    # Encode the plot image as base64
    plot_base64 = base64.b64encode(plot_img.read()).decode('utf-8')

    return render_template('plot.html', plot_base64=plot_base64)

if __name__ == '__main__':
    app.run(debug=True)
