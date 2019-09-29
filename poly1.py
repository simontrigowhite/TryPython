# -*- coding: utf-8 -*-
"""
Created on Sun Sep 29 17:30:56 2019

@author: Simon
"""

# First try polynomial regression AI

from numpy import loadtxt
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures

# load the dataset
dataset = loadtxt(
        'C:/Users/Simon/Documents/GitHub/TryPython/poly1.csv',
        delimiter=',')

# split into input (X) and output (y) variables
X = dataset[:, 0:1]
y = dataset[:, 1]

# Fitting Polynomial Regression to the dataset
poly_reg = PolynomialFeatures(degree=2)
X_poly = poly_reg.fit_transform(X)
pol_reg = LinearRegression()
pol_reg.fit(X_poly, y)

y_pred_155 = pol_reg.predict(poly_reg.fit_transform([[15.5]]))
print('Prediction of 15.5: %.2f' % y_pred_155)

y_preds = pol_reg.predict(poly_reg.fit_transform(X))

plt.scatter(X, y, color='red')
plt.scatter([[15.5]], y_pred_155, color='green', zorder=10, s=75)
plt.plot(X, pol_reg.predict(poly_reg.fit_transform(X)), color='blue')
plt.show()
