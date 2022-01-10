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
