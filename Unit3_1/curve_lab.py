import matplotlib.pyplot as plt

mass_list = [20,40,60,80,100,120]
temp_list = [10,18.2,46,65,67.5,70]

plt.plot(mass_list, temp_list, color='blue')
plt.grid(axis='both')
plt.title(label='Temperature Curve')
plt.xlabel('Mass(g)')
plt.ylabel('Temperature(celcius)')
plt.show()