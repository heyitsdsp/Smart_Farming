# -*- coding: utf-8 -*-
"""
Created on Sat Oct 17 15:07:59 2020

@author: bambo
"""
import Fert_Dataset as fd
import os

def Predict_Fertiliser(sensor_value):
    loc_Fert = os.getcwd() + r'/Datasets/FertPredictDataset.csv'
    
    dataset = fd.get_fert_dataset(loc_Fert)
    
    X = dataset.iloc[:, :3].values
    Y = dataset.iloc[:, 3].values
    
    from sklearn.model_selection import train_test_split
    
    X_train, X_test, Y_train, Y_test = train_test_split(X, Y,
                                                        test_size = 0.2, 
                                                        random_state = 0)
    
    from sklearn.tree import DecisionTreeClassifier
    dtree_model = DecisionTreeClassifier(max_depth = 2).fit(X_train, 
                                                            Y_train)
    
    dtree_pred = dtree_model.predict(sensor_value)
    
    return dtree_pred





