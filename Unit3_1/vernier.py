import gdx

gdx = gdx.gdx()

gdx.open_usb()
gdx.select_sensors([2,3])
gdx.start()

for i in range(40):
    measure = gdx.read()
    if measure == None:
        break
    print(measure)

gdx.stop()
gdx.close()