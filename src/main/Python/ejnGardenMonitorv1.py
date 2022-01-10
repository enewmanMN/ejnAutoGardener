#/usr/bin/env python3
import serial
import time
import csv
import matplotlib
matplotlib.use("tkAgg")
import matplotlib.pyplot as plt
import numpy as np
import mpld3
import pandas as pd
from flask import Flask
app = Flask(__name__)

@app.route('/')
def index():
    return "Gardener V1 - /moisture, /temperature etc"


@app.route('/moisture')
def getMoisture():
    plot_window = 20
    data= pd.read_csv("soilData.csv") #data.columns has columns, can get individual rows by column etc
    y_var = data.soilReading[-plot_window:]
    plt.ion()
    fig, ax = plt.subplots()
    line, = ax.plot(y_var)
    ax.relim()
    ax.autoscale_view()
    return mpld3.show()

if __name__ == '__main__':
    app.run(debug=True, port=80, host='0.0.0.0')


