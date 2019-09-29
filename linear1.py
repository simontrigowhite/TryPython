# -*- coding: utf-8 -*-
"""
Created on Sat Sep 28 23:38:32 2019

@author: Simon
"""

# First try linear regression AI

from numpy import loadtxt
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

# load the dataset
dataset = loadtxt(
        'C:/Users/Simon/Documents/GitHub/TryPython/linear1.csv',
        delimiter=',')

# split into input (X) and output (y) variables
X = dataset[:, 0:1]
y = dataset[:, 1]

# Fitting Simple Linear Regression to the Training set
regressor = LinearRegression()
regressor.fit(X, y)

y_pred_155 = regressor.predict([[15.5]])
print('Prediction of 15.5: %.2f' % y_pred_155)

y_preds = regressor.predict(X)

plt.scatter(X, y, color='red')
plt.scatter([[15.5]], y_pred_155, color='green', zorder=10, s=75)
plt.plot(X, regressor.predict(X), color='blue')
plt.show()
