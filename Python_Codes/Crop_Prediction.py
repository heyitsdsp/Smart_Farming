# -*- coding: utf-8 -*-
"""
Created on Fri Oct 16 02:19:00 2020

@author: bambo
"""
import Dataset as ds
import Sensor_values as sv
import os
import matplotlib.pyplot as plt
import numpy as np

# GET THE DATASET INTO THE CODE
loc = os.getcwd() + r'/Datasets/Crop_Pred.csv'
data_details = ds.get_data_details(loc)

dataset = data_details[0]
crop_value_pairs = data_details[1]

# GET THE SENSOR VALUES INTO THE CODE
sensor_values = sv.get_readings()
user_location = sensor_values[0]
sensor_values = sensor_values[1]

# PREPARE THE MATRIX OF FEATURES AND OUTPUT MATRIX
X = dataset.iloc[:, 1:].values
Y = dataset.iloc[:, 0].values

# SPLIT X AND Y INTO THE TRAINING SET AND TEST SET
from sklearn.model_selection import train_test_split
X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size = 0.2,
                                                    random_state = 0)
"""
# MULTIPLE LINEAR REGRESSION
from sklearn.linear_model import LinearRegression
regressor = LinearRegression()
regressor.fit(X_train, Y_train)

Y_pred = regressor.predict(X_test)
np.set_printoptions(precision = 2)
print(np.concatenate((Y_pred.reshape(len(Y_pred), 1), 
                      Y_test.reshape(len(Y_pred), 1)), axis = 1))
"""

"""
# PLOYNOMIAL REGRESSION
from sklearn.preprocessing import PolynomialFeatures
from sklearn.linear_model import LinearRegression

# Go for a polynomial of degree 4 but 20 is good as well
poly_reg = PolynomialFeatures(degree = 4)
X_train_poly = poly_reg.fit_transform(X_train)
poly_model = LinearRegression()
poly_model.fit(X_train_poly, Y_train)

Y_pred = poly_model.predict(poly_reg.fit_transform(X_test))
for i in range(0, len(Y_pred)):
    Y_pred[i] = round(Y_pred[i])
    
Y_pred = Y_pred.astype('int')
np.set_printoptions(precision = 2)
print(np.concatenate((Y_pred.reshape(len(Y_pred), 1), 
                      Y_test.reshape(len(Y_pred), 1)), axis = 1))    
"""

"""
# BAYESIAN RIDGE REGRESSION
from sklearn.linear_model import BayesianRidge
bay_ridge = BayesianRidge()
bay_ridge.fit(X_train, Y_train)
Y_pred = bay_ridge.predict(X_test)

np.set_printoptions(precision = 2)
print(np.concatenate((Y_pred.reshape(len(Y_pred), 1), 
                      Y_test.reshape(len(Y_pred), 1)), axis = 1))
"""

# ARTIFICIAL NEURAL NETWORK USING TENSORFLOW 2.0
import tensorflow as tf



