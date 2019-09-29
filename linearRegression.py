# -*- coding: utf-8 -*-
"""
Created on Sun Sep 29 13:22:21 2019

@author: Simon
"""

# https://towardsdatascience.com/machine-learning-simple-linear-regression-with-python-f04ecfdadc13

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split

# Importing the dataset
dataset = pd.read_csv('salary_data.csv')
X = dataset.iloc[:, :-1].values  # get a copy of dataset exclude last column
y = dataset.iloc[:, 1].values  # get array of dataset in column 1st

# Splitting the dataset into the Training set and Test set
X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=1/3, random_state=0)

# Fitting Simple Linear Regression to the Training set
regressor = LinearRegression()
regressor.fit(X_train, y_train)

# Visualizing the Training set results
viz_train = plt
viz_train.scatter(X_train, y_train, color='red')
viz_train.plot(X_train, regressor.predict(X_train), color='blue')
viz_train.title('Salary VS Experience (Training set)')
viz_train.xlabel('Year of Experience')
viz_train.ylabel('Salary')
viz_train.show()

# Visualizing the Test set results
viz_test = plt
viz_test.scatter(X_test, y_test, color='red')
viz_test.plot(X_train, regressor.predict(X_train), color='blue')
viz_test.title('Salary VS Experience (Test set)')
viz_test.xlabel('Year of Experience')
viz_test.ylabel('Salary')
viz_test.show()

# Predicting the result of 5 Years Experience
y_pred = regressor.predict([[5]])
print(y_pred)

# Predicting the Test set results
y_preds_test = regressor.predict(X_test)
print(y_preds_test)

# Visualizing the predicted results of the test set
viz_predicted_test = plt
viz_predicted_test.scatter(X_test, y_test, color='red')
viz_predicted_test.scatter(X_test, y_preds_test, color='blue')
viz_predicted_test.plot(X_train, regressor.predict(X_train), color='blue')
viz_predicted_test.show()

# Predicting the training set results
y_preds_train = regressor.predict(X_train)
print(y_preds_train)

# Visualizing the predicted results of the training set
viz_predicted_train = plt
viz_predicted_train.scatter(X_train, y_train, color='red')
viz_predicted_train.scatter(X_train, y_preds_train, color='blue')
viz_predicted_train.plot(X_train, regressor.predict(X_train), color='blue')
viz_predicted_train.show()
