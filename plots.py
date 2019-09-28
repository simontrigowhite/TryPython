# -*- coding: utf-8 -*-
"""
Created on Sat Sep 28 21:17:40 2019

@author: Simon
"""

import numpy as np
import matplotlib.pyplot as plt

x = np.arange(0, 20, 0.01)
y = np.sin(x)
z = np.cos(x)

fig_size = plt.rcParams["figure.figsize"]
fig_size[0] = 10
fig_size[1] = 5
plt.rcParams["figure.figsize"] = fig_size

plt.plot(x, y, label="sin")
plt.plot(x, z, label="cos")
plt.legend(loc='upper center')

plt.xticks(np.arange(min(x), max(x)+1, np.pi / 2))

plt.show()
