#/usr/bin/env python3
import serial
import time
import csv
import matplotlib
matplotlib.use("tkAgg")
import matplotlib.pyplot as plt
import numpy as np
import mpld3
from flask import Flask
app = Flask(__name__)

@app.route('/')
def index():
    return "Hello world"


@app.route('/moisture')
def getMoisture():
    ser = serial.Serial('/dev/ttyACM0', 9600, timeout=1)
    ser.reset_input_buffer()

    plot_window = 20
    y_var = np.array(np.zeros([plot_window]))

    plt.ion()
    fig, ax = plt.subplots()
    line, = ax.plot(y_var)

    while True:
        if ser.in_waiting > 0:
            ser_bytes = ser.readline()
            decoded_bytes = float(ser_bytes[0:len(ser_bytes)-2].decode("utf-8"))
            if line is not '':
                print(decoded_bytes)
                with open("test_data.csv","a") as f:
                    writer = csv.writer(f,delimiter=",")
                    writer.writerow([time.time(),decoded_bytes])
                y_var = np.append(y_var,decoded_bytes)
                y_var = y_var[1:plot_window+1]
                line.set_ydata(y_var)
                ax.relim()
                ax.autoscale_view()
                fig.canvas.draw()
                fig.canvas.flush_events()
                return mpld3.show()
            else:
                print("nothing to read")

if __name__ == '__main__':
    app.run(debug=True, port=80, host='0.0.0.0')


