# Question_1b_and_1c.py
# Somesh Herath Bandara
# Taylor Olsen
# Travis Lawrence

from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

m = 2**32
a = 65539
zdata =[]
xdata =[]
ydata =[]
alldata = []

previous = 1
for i in range(10000):
    mod = (a*previous) % m
    previous = mod
    xdata.append(previous)
    alldata.append(previous)

    mod = (a*previous) % m
    previous = mod
    ydata.append(previous)
    alldata.append(previous)

    mod = (a*previous) % m
    previous = mod
    zdata.append(previous)
    alldata.append(previous)

ax.scatter(xdata, ydata, zdata, c='r', marker='o', label = "Data Points")

ax.set_xlabel('X Axis')
ax.set_ylabel('Y Axis')
ax.set_zlabel('Z Axis')

plt.title('3D Plot of RANDU Values')
plt.legend()
plt.show()


plt.hist(alldata, bins=30, label = "Values")
plt.ylabel('Number of Points')
plt.xlabel('Bins')
plt.title('Histogram with 30 Bins Containing RANDU Values')
plt.legend()
plt.show()