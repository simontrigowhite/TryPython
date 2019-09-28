# -*- coding: utf-8 -*-
"""
Created on Fri Sep 27 22:48:37 2019

@author: Simon
"""

# https://machinelearningmastery.com/machine-learning-in-python-step-by-step/

# Load libraries
import pandas
from pandas.plotting import scatter_matrix
import matplotlib.pyplot as plt

# Load dataset
url = "C:/Users/Simon/Documents/GitHub/TryPython/iris.csv"
names = ['sepal-length', 'sepal-width', 'petal-length', 'petal-width', 'class']
dataset = pandas.read_csv(url, names=names)

# shape
print(dataset.shape)

# head
print(dataset.head(20))

# descriptions
print(dataset.describe())

# class distribution
print(dataset.groupby('class', sort=False).size())

# box and whisker plots
dataset.plot(
        kind='box', subplots=True, layout=(2, 2), sharex=False, sharey=False)
plt.show()

# histograms
dataset.hist()
plt.show()

# scatter plot matrix
scatter_matrix(dataset)
plt.show()
