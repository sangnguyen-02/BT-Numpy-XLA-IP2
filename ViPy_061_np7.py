import numpy as np

url = "https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data"
data = np.genfromtxt(url, delimiter=',', usecols=(0))
mean = np.mean(data)
median = np.median(data)
stddev = np.std(data)

print("Mean của SepalLength:", mean)
print("Median của SepalLength:", median)
print("Standard Deviation của SepalLength:", stddev)
