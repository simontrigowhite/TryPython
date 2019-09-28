# -*- coding: utf-8 -*-
"""
Created on Sat Sep 28 23:38:32 2019

@author: Simon
"""

from numpy import loadtxt
from keras.models import Sequential
from keras.layers import Dense

# load the dataset
dataset = loadtxt(
        'C:/Users/Simon/Documents/GitHub/TryPython/linear1.csv',
        delimiter=',')
# split into input (X) and output (y) variables
xs = dataset[:, 0]
ys = dataset[:, 1]

# define the keras model
model = Sequential()
model.add(Dense(1, input_dim=1, activation='relu'))
#model.add(Dense(8, activation='relu'))
#model.add(Dense(1, activation='sigmoid'))

# compile the keras model
model.compile(
        loss='mean_squared_error', optimizer='sgd', metrics=['accuracy'])

# fit the keras model on the dataset
model.fit(xs, ys, epochs=150, batch_size=5)

# evaluate the keras model
loss, accuracy = model.evaluate(xs, ys)
print('Accuracy: %.2f' % (accuracy*100))

# gives accuracy of 0!
