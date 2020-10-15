# -*- coding: utf-8 -*-
"""
Created on Fri Oct 16 02:19:00 2020

@author: bambo
"""
import Dataset as ds
import Sensor_values as sv
import os
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split

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
X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size = 0.2,
                                                    random_state = 0)


