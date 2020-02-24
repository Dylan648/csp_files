import matplotlib.pyplot as plt

path = 'data_files/light.csv'

with open(path) as f:
    data = f.read().split('\n')

fig,ax = plt.subplots(1,3)

time = []
nm615 = []
nm525 = []
nm465 = []

for item in data[1:]:
    num = item.split(',')
    current_time = float(num[0])
    time.append(current_time)
    nm615.append(num[1])
    nm525.append(num[2])
    nm465.append(num[3])

ax[0][0].plot(time, nm525)
plt.plot(time, nm465)
plt.yticks(range(0,40,1))
plt.show()