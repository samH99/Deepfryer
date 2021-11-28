# 402Project1_Question_6.py
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

previous = 1
for i in range(1000):
    mod = (a*previous) % m
    previous = mod
    xdata.append(previous)

    mod = (a*previous) % m
    previous = mod
    ydata.append(previous)

    mod = (a*previous) % m
    previous = mod
    zdata.append(previous)

ax.scatter(xdata, ydata, zdata, c='r', marker='o')

ax.set_xlabel('X Label')
ax.set_ylabel('Y Label')
ax.set_zlabel('Z Label')

plt.show()