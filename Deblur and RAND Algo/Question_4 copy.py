# Question_4.py
# Somesh Herath Bandara
# Taylor Olsen
# Travis Lawrence

import math
import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import curve_fit

t = np.array([1971.,1972.,1974.,1978.,1982.,1985.,1989.,1993.,1997.,1999.,2000.,2002.,2003.])
b = np.array([2250,2500,5000,29000,120000,275000,1180000,3100000,7500000,24000000,42000000,220000000,410000000])

# Part B
tp = np.linspace(1970,2015,13)
plt.semilogy()

def graph(formula, x_range):
    x = np.arange(*x_range)
    y = eval(formula)
    plt.plot(x, y, "r-")

graph('3.125*(pow(10,(.154*(x-1970))))', (1970,2015))

print(3.125*(pow(10,(.154*(2015-1970)))))
#part 3 26598063.6938

plt.plot(t,b,'k*', marker = '+')

plt.xlabel('Time (years)', fontsize = 16)
plt.ylabel('Transistors', fontsize = 16)



plt.show()