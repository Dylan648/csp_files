import matplotlib.pyplot as plt

path = 'data_files/morse_code.csv'

with open(path) as f:
    data = f.read().split('\n')

time = []
decibels1 = []
decibels2 = []

for item in data[1:]:
    num = item.split(',')
    current_time = float(num[0])
    if current_time < 35 and int(current_time*10) % 2 == 0:
        time.append(current_time)
        decibels1.append(float(num[1]))
        decibels2.append(float(num[2]))

plt.plot(time, decibels1)
plt.plot(time, decibels2)
plt.xticks(range(0,40,1))
plt.show()