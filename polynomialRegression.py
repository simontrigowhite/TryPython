# -*- coding: utf-8 -*-
"""
Created on Sun Sep 29 14:20:37 2019

@author: Simon
"""

# https://towardsdatascience.com/machine-learning-polynomial-regression-with-python-5328e4e8a386

import matplotlib.pyplot as plt
import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures

# Importing the dataset
dataset = pd.read_csv('position_salaries.csv')
X = dataset.iloc[:, 1:2].values
y = dataset.iloc[:, 2].values

# Splitting the dataset into the Training set and Test set
X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=0)

# Fitting Linear Regression to the dataset
lin_reg = LinearRegression()
lin_reg.fit(X, y)

# Fitting Polynomial Regression to the dataset
poly_reg = PolynomialFeatures(degree=4)
X_poly = poly_reg.fit_transform(X)
pol_reg = LinearRegression()
pol_reg.fit(X_poly, y)

# Predicting a new result with Linear Regression
linear_predict_55 = lin_reg.predict([[5.5]])
print("Linear for 5.5: %.2f" % linear_predict_55)
# output should be 249500

# Predicting a new result with Polymonial Regression
poly_predict_55 = pol_reg.predict(poly_reg.fit_transform([[5.5]]))
print("Poly for 5.5: %.2f" % poly_predict_55)
# output should be 132148.43750003


# Visualizing the Linear Regression results
def viz_linear():
    plt.scatter(X, y, color='red')
    plt.scatter([[5.5]], linear_predict_55, color='green', zorder=10, s=75)
    plt.plot(X, lin_reg.predict(X), color='blue')
    plt.title('Truth or Bluff (Linear Regression)')
    plt.xlabel('Position level')
    plt.ylabel('Salary')
    plt.show()
    return
viz_linear()


# Visualizing the Polymonial Regression results
def viz_polymonial():
    plt.scatter(X, y, color='red')
    plt.scatter([[5.5]], poly_predict_55, color='green', zorder=10, s=75)
    plt.plot(X, pol_reg.predict(poly_reg.fit_transform(X)), color='blue')
    plt.title('Truth or Bluff (Linear Regression)')
    plt.xlabel('Position level')
    plt.ylabel('Salary')
    plt.show()
    return
viz_polymonial()
