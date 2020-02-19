import matplotlib.pyplot as plt

path = '../data_files/raw_data_311.csv'

'''this opens the file and seperates each line on the new line character and
def data var'''
with open(path) as f:
    data = f.read().split('\n')

#initalizes 3 lists
time_list = []
temp1_list = []
temp2_list = []

''' this loops through the data and seperates each set of data and puts it
in the correct list'''
for item in data[1:]:
    vals = item.split(',')
    time_list.append(int(vals[0]))
    temp1_list.append(float(vals[1]))
    temp2_list.append(float(vals[2]))

plt.plot(time_list, temp1_list, color='blue')
plt.plot(time_list, temp2_list, color='red')
plt.grid(axis='both')
plt.xticks(range(0, max(time_list)+25, 25))
plt.title(label='Data Set 4')
plt.xlabel('Time(seconds)')
plt.ylabel('Temp(celcius)')
plt.show()