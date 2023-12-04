# -*- coding: utf-8 -*-
"""
Created on Tue Apr 12 13:56:30 2022

@author: user
"""

import numpy as np
import matplotlib.pyplot as plt
from tensorflow import keras
from pandas import read_csv
import tensorflow as tf
import math
import pickle
from keras.models import Model
#from keras.utils import plot_model
from sklearn.preprocessing import MinMaxScaler
from sklearn.model_selection import train_test_split
print ('TensorFlow version: ' + tf.__version__)

# Create noisy data
'''
x_data = np.linspace(-1, 6, num=10)
print(x_data)
y_data = 0.1*np.cos(x_data)+.4*x_data**2
print('Data created successfully')
'''
url = 'C:\B.project_MM\Variable project_3\Sample results.csv'
dataframe = read_csv(url, header=None)
#train, test = train_test_split(dataframe, test_size=0.2)
data = dataframe.values
scaler=MinMaxScaler()
scaler.fit(data)
data=scaler.transform(data)
# choose the input and output variables
x, y = data[:, [0, 1,2]], data[:, 5]
x_data,x_test, y_data, y_test = train_test_split(x, y, test_size=0.3)
y_data=np.reshape(y_data,(-1,1))

# Display the dataset
#plt.scatter(x_data[::1], y_data[::1])
#plt.grid()
#plt.show()

# Create the model 
model = keras.Sequential()
model.add(keras.layers.Dense(units = 1, activation = 'linear', input_shape=[3]))
model.add(keras.layers.Dense(units = 64, activation = 'relu'))
model.add(keras.layers.Dense(units = 64, activation = 'relu'))
model.add(keras.layers.Dense(units = 1, activation = 'linear'))

model.compile(loss='mse', optimizer="adam",metrics=["accuracy"])

# Display the model
model.summary()
# Training
result=model.fit( x_data, y_data, epochs=1200, verbose=1,
                    validation_data=(x_test, y_test))
plt.plot(result.history['loss'])
# Compute the output 
y_predicted = model.predict(x_test)
train_score = model.evaluate(x, y, verbose=True)
test_score = model.evaluate(x_test, y_test, verbose=True)
# Display the result
plt.figure(figsize=(8,5))
plt.scatter(x_test[:,0], y_test)
plt.plot(x_test[:,0], y_predicted, 'r', linewidth=2)
plt.grid()
plt.show()
xp=[.6,.358593551,.474398526]
xp=np.reshape(xp,(1,3))
a=model.predict(xp)
plt.ion()
fig = plt.figure()
subfig = fig.add_subplot(122)
subfig.plot(result.history['accuracy'], label="training")
if result.history['val_accuracy'] is not None:
    subfig.plot(result.history['val_accuracy'], label="validation")
subfig.set_title('Model Accuracy')
subfig.set_xlabel('Epoch')
subfig.legend(loc='upper left')
subfig = fig.add_subplot(121)
subfig.plot(result.history['loss'], label="training")
if result.history['val_loss'] is not None:
    subfig.plot(result.history['val_loss'], label="validation")
subfig.set_title('Model Loss')
subfig.set_xlabel('Epoch')
subfig.legend(loc='upper left')
plt.ioff()

#model.save('Modelrf')

    
    
    
    