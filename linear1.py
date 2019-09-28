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
        'C:/Users/Simon/Documents/GitHub/TryPython/linear2.csv',
        delimiter=',')
# split into input (X) and output (y) variables
xs = dataset[:, 0:8]
ys = dataset[:, 8]

# define the keras model
model = Sequential()
model.add(Dense(12, input_dim=8, activation='relu'))
model.add(Dense(8, activation='relu'))
model.add(Dense(1, activation='sigmoid'))

# compile the keras model
model.compile(
        loss='mean_squared_error', optimizer='adam', metrics=['accuracy'])

# fit the keras model on the dataset
model.fit(xs, ys, epochs=150, batch_size=10)

# evaluate the keras model
loss, accuracy = model.evaluate(xs, ys)
print('Accuracy: %.2f' % (accuracy*100))

# gives accuracy of 0! loss doesn't reduce over epochs.

model.summary()

# and only 221 params!
