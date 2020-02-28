import gdx, matplotlib.pyplot as plt

gdx = gdx.gdx()

samples = int(input('How many samples would you like to take?: '))

gdx.open_usb()
gdx.select_sensors([2,3])
gdx.start(period=100)

sound_a, sound_c, time = [], [], []
count = 0

for i in range(samples):
    measure = gdx.read()
    sound_a.append(measure[0])
    sound_c.append(measure[1])
    time.append(count)
    count += 1
    plt.ion()
    plt.gcf()
    plt.plot(sound_a, color='red')
    plt.plot(sound_c, color='green')
    plt.draw()
    plt.pause(.05)

    if measure == None:
        break


#plots this data on one graph
plt.plot(time, sound_a)#graphs the a sounds
plt.plot(time, sound_c)#graphs the c sounds
plt.title(label='Vernier')
plt.show()
gdx.stop()
gdx.close()