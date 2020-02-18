path = 'data_files/raw_data_311.csv'

with open(path) as f:
    data = f.read().split('\n')

time_list = []
temp1_list = []
temp2_list = []

for item in data[1:]:
    vals = item.split(',')
    time_list.append(int(vals[0]))
    temp1_list.append(float(vals[1]))
    temp2_list.append(float(vals[2]))

