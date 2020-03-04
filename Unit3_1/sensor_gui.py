from tkinter import *
import gdx, matplotlib.pyplot as plt, numpy as np
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

gdx = gdx.gdx()
gdx.open_usb()

sound_a, sound_c = [], []
def start_reading():
    seconds = int(seconds_field.get())
    samples = int(samples_field.get())
    sound_a, sound_c = [], []
    rate = 1000 // samples
    gdx.start(rate)
    interval = 1 / samples
    length = np.arange(0, seconds, interval)
    ax.cla()
    for i in range(samples * seconds):
        measure = gdx.read()
        sound_a.append(measure[0])
        sound_c.append(measure[1])
        if measure == None:
            break

    plt.yscale('linear')
    ax.plot(length, sound_a, c='red')
    ax.plot(length, sound_c, c='blue')
    plt.ylabel(ylabel='Sound(decibels)')
    plt.xlabel(xlabel='Time(seconds)')
    plt.show()
    gdx.stop()
    
root = Tk()

seconds_label = Label(root, text='How many seconds?')
seconds_label.grid(row=0, column=0)
seconds_field = Entry(root)
seconds_field.grid(row=1,column=0)

samples_label = Label(root, text='How many samples / seconds?')
samples_label.grid(row=2, column=0)
samples_field = Entry(root)
samples_field.grid(row=3, column=0)

# sensor_label = Label(root, text='What sensor(s) would you like to use?')
# sensor_label.pack()
# sensor_field = Entry(root)
# sensor_field.pack()

# sensor_list = []
# for choice in sensor_field.get():
#     num = choice.split(' ')
#     sensor_list.append(num)
gdx.select_sensors([2,3])

start_button = Button(root, text='Start Sensing', command=start_reading)
start_button.grid(row=4, column=0)

fig, ax = plt.subplots(1,1)
plt.ion()
chart = FigureCanvasTkAgg(fig, root)
chart.get_tk_widget().grid(row=0, column=1, rowspan=20)

root.mainloop()