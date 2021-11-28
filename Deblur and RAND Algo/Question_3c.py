# Question_3c.py
# Somesh Herath Bandara
# Taylor Olsen
# Travis Lawrence

import matplotlib.pyplot as plt
import numpy as np
import math
from random import random

values = []

for i in range(1000):
    x = random()
    if(x <= 1/2):
        values.append(math.log(2*(x)))
    elif(x > 1/2):
        values.append(-math.log(2*(1-x)))

fig, axs = plt.subplots(2)
fig.suptitle('Histogram and PDF')

x = np.arange(-10, 10, .001) 

axs[0].hist(values, label = "Samples")

x = np.arange(-6, 0, .001) 
x2 = np.arange(0, 6, .001) 
axs[1].plot(x, np.exp(2*x), 'r', label = "PDF") 
axs[1].plot(x2, np.exp(-2*x), 'r') 

axs[0].set(xlabel='Bins', ylabel='Number of Samples')
axs[1].set(xlabel='Y Axis', ylabel='X Axis')

axs[0].legend()
axs[1].legend()
plt.show()