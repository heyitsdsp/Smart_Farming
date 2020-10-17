# -*- coding: utf-8 -*-
"""
Created on Sat Oct 17 22:07:14 2020

@author: bambo
"""
import Dataset as ds
import os

def Predict_Crop(sensor_value):
    loc = os.getcwd() + r'/Datasets/Crop_Pred.csv'
    
    # GET THE TRAINING AND TEST DATA
    training_details = ds.get_training_crop_details(loc)
    
    # TRAINING PART
    training_dataset = training_details[0]
    crop_value_pairs = training_details[1]
    
    # PREPARE THE MATRIX OF FEATURES AND THE OUTPUT MATRIX
    X_train = training_dataset.iloc[:, 1:].values
    Y_train = training_dataset.iloc[:, 0].values
    
    # MULTILINEAR REGRESSION
    from sklearn.linear_model import LinearRegression
    
    # PREPARE LINEAR REGRESSION MODEL
    model = LinearRegression()
    model.fit(X_train, Y_train)
    
    
    # PREDICTION PART
    Y_pred = model.predict([sensor_value])
    Y_pred = Y_pred.astype('int')

    return [Y_pred, crop_value_pairs]

