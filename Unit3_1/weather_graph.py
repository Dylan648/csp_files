import matplotlib.pyplot as plt

path = 'data_files/weather.csv'
days = 0
with open(path) as f:
    data = f.read().strip().split('\n')

fig, ax = plt.subplots(2,3)
fig.tight_layout(pad=3)

actual_mean = []
actual_min_temp = []
actual_max_temp = []
actual_precip = []
record_min_temp = []
record_max_temp = []
days_since_july1 = []

for item in data[1:]:
    num = item.split(',') 
    actual_mean.append(int(num[1]))
    actual_min_temp.append(int(num[2]))
    actual_max_temp.append(int(num[3]))
    actual_precip.append(float(num[10]))
    record_max_temp.append(int(num[7]))
    record_min_temp.append(int(num[6]))
    days_since_july1.append(days)
    days += 1

ax[0][0].plot(days_since_july1, actual_mean, color='purple')
ax[0][0].set(title='Actual mean temperature', ylabel='Temp(Fahrenheit)')

ax[0][1].plot(days_since_july1, actual_max_temp, color='red')
ax[0][1].set(title='Actual max temperature', ylabel='Temp(Fahrenheit)')

ax[0][2].plot(days_since_july1, actual_min_temp, color='blue')
ax[0][2].set(title='Actual min temperature', ylabel='Temp(Fahrenheit)')

ax[1][0].plot(days_since_july1, actual_precip, color='gray')
ax[1][0].set(title='Actual precipitation', ylabel='Inches')

ax[1][1].plot(days_since_july1, record_max_temp, color='red')
ax[1][1].set(title='Record max temperature', ylabel='Temp(Fahrenheit)')

ax[1][2].plot(days_since_july1, record_min_temp, color='blue')
ax[1][2].set(title='Record min temperature', ylabel='Temp(Fahrenheit)')

plt.yscale('linear')
plt.show()