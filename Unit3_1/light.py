import matplotlib.pyplot as plt

path = 'data_files/light.csv'

with open(path) as f:
    data = f.read().split('\n')