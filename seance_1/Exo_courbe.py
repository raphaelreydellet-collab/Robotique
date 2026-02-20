import matplotlib.pyplot as plot
import time
import warnings
import sys

sys.tracebacklimit = 0
warnings.filterwarnings("ignore", ".*GUI is implemented.*")

# plot data
x_data = []
y_data = []

if __name__ == '__main__':
    plot.autoscale()
    plot.show(block=False)
    plot_handle, = plot.plot([-1, 70], [-1, 4000], marker='o', color='red')
    try:
        for i in range(60):
            x_data.append(i)
            y_data.append(i * i)
            plot_handle.set_xdata(x_data)
            plot_handle.set_ydata(y_data)
            plot.draw()
        while True:
            plot.pause(0.05)
    except KeyboardInterrupt:
        time.sleep(1)
        plot.close()
        print("Fin du programme\n")
        pass
