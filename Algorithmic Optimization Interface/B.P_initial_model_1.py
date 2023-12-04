# -*- coding: utf-8 -*-
"""
Created on Tue Mar 22 18:23:21 2022

@author: MAINAK
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
data = dataframe.values
scaler=MinMaxScaler()
scaler.fit(data)
data=scaler.transform(data)
# choose the input and output variables
x_data, y_data = data[:, [0, 1,2]], data[:, 4]

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

model.compile(loss='mse', optimizer="adam")

# Display the model
model.summary()
# Training
result=model.fit( x_data, y_data, epochs=1200, verbose=1)
plt.plot(result.history['loss'])
# Compute the output 
y_predicted = model.predict(x_data)

# Display the result
plt.figure(figsize=(8,5))
plt.scatter(data[:,0], y_data)
plt.plot(data[:,0], y_predicted, 'r', linewidth=2)
plt.grid()
plt.show()
xp=[.6,.358593551,.474398526]
xp=np.reshape(xp,(1,3))
a=model.predict(xp)

#model.save('Modelenergy')

    
    
    
    