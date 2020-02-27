import gdx, matplotlib.pyplot as plt

gdx = gdx.gdx()

gdx.open_usb()
gdx.select_sensors([2,3])
gdx.start()

sound_a, sound_c = [], []

for i in range(5):
    measure = gdx.read()
    if measure == None:
        break
    sound_a.append(float(measure[0]))
    sound_c.append(float(measure[1]))

print(sound_a)
print(sound_c)

gdx.stop()
gdx.close()

#prewrite(no testing available)might not work
#plots this data on one graph
ply.plot(len(sound_a), sound_a)#graphs the a sounds
ply.plot(len(sound_a), sound_c)#graphs the c sounds
plt.title(label='Vernier')
plt.show()