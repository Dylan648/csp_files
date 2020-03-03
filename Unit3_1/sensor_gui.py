from tkinter import *
import gdx, matplotlib.pyplot as plt, numpy as np

gdx = gdx.gdx()
gdx.open_usb()
gdx.select_sensors([2,3])

sound_a, sound_c = [], []
def start_reading():
    seconds = int(seconds_field.get())
    samples = int(samples_field.get())
    sound_a, sound_c = [], []
    rate = 1000 // samples
    gdx.start(rate)
    interval = 1 / samples
    length = np.arange(0, seconds, interval)
    for i in range(samples * seconds):
        measure = gdx.read()
        sound_a.append(measure[0])
        sound_c.append(measure[1])
        if measure == None:
            break

    plt.yscale('linear')
    plt.plot(length, sound_a, c='red')
    plt.plot(length, sound_c, c='blue')
    plt.show()
    gdx.stop()
    



root = Tk()

seconds_label = Label(root, text='How many seconds?')
seconds_label.pack()
seconds_field = Entry(root)
seconds_field.pack()

samples_label = Label(root, text='How many samples / seconds?')
samples_label.pack()
samples_field = Entry(root)
samples_field.pack()

start_button = Button(root, text='Start Sensing', command=start_reading)
start_button.pack()

root.mainloop()