# -*- coding: utf-8 -*-
"""
Created on Sat Sep 28 21:17:40 2019

@author: Simon
"""

import numpy as np
import matplotlib.pyplot as plt

x = np.arange(0, 10, 0.01)
y = np.sin(x)

fig_size = plt.rcParams["figure.figsize"]
fig_size[0] = 18
fig_size[1] = 12
plt.rcParams["figure.figsize"] = fig_size

plt.plot(x, y)
