import gdx, matplotlib.pyplot as plt

gdx = gdx.gdx()

gdx.open_usb()
gdx.select_sensors([2,3])
gdx.start()

sound_a, sound_c, time = [], [], []
count = 0

for i in range(5):
    measure = gdx.read()
    if measure == None:
        break
    sound_a.append(float(measure[0]))
    sound_c.append(float(measure[1]))
    time.append(count)
    count += 1

gdx.stop()
gdx.close()


#prewrite(no testing available)might not work
#plots this data on one graph
ply.plot(time, sound_a)#graphs the a sounds
ply.plot(time, sound_c)#graphs the c sounds
plt.title(label='Vernier')
plt.show()