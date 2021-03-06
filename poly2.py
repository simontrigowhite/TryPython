# -*- coding: utf-8 -*-
"""
Created on Sun Sep 29 17:52:11 2019

@author: Simon
"""

# polynomial - cubic

from numpy import loadtxt
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures

# load the dataset
dataset = loadtxt(
        'C:/Users/Simon/Documents/GitHub/TryPython/poly2.csv',
        delimiter=',')

# split into input (X) and output (y) variables
X = dataset[:, 0:1]
y = dataset[:, 1]

# Fitting Polynomial Regression to the dataset
regressor = LinearRegression()
poly_reg = PolynomialFeatures(degree=3)
X_poly = poly_reg.fit_transform(X)
regressor.fit(X_poly, y)

x_test = 7.5
y_pred_test = regressor.predict(poly_reg.fit_transform([[x_test]]))
print('Prediction of %.2f: %.2f' % (x_test, y_pred_test))

y_preds = regressor.predict(X_poly)

plt.scatter(X, y, color='red')
plt.scatter([[x_test]], y_pred_test, color='green', zorder=10, s=75)
plt.plot(X, regressor.predict(X_poly), color='blue')
plt.show()

print(X_poly)

print(regressor.coef_)
