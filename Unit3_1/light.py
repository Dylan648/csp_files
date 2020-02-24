import matplotlib.pyplot as plt

path = 'data_files/light.csv'

with open(path) as f:
    data = f.read().split('\n')

fig,ax = plt.subplots(3,1)
fig.tight_layout(pad=3)

time = []
nm615 = []
nm525 = []
nm465 = []

for item in data[1:]:
    num = item.split(',')
    current_time = float(num[0])
    time.append(current_time)
    nm615.append(float(num[1]))
    nm525.append(float(num[2]))
    nm465.append(float(num[3]))

ax[0].plot(time, nm615, c='red')
ax[0].set(title='615 nm', ylabel='lux')
ax[1].plot(time, nm525, c='blue')
ax[1].set(title='525 nm', ylabel='lux')
ax[2].plot(time, nm465, c='green')
ax[2].set(title='465 nm', ylabel='lux')
plt.xlabel(xlabel='time(seconds)')
plt.xscale('linear')
plt.yscale('linear')
plt.show()