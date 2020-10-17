# -*- coding: utf-8 -*-
"""
Created on Sat Oct 17 15:04:31 2020

@author: bambo
"""


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
# BAYESIAN RIDGE REGRESSION
from sklearn.linear_model import BayesianRidge
bay_ridge = BayesianRidge()
bay_ridge.fit(X_train, Y_train)
Y_pred = bay_ridge.predict(X_test)

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

np.set_printoptions(precision = 2)
print(np.concatenate((Y_pred.reshape(len(Y_pred), 1), 
                        Y_test.reshape(len(Y_pred), 1)), axis = 1))    
 """   
 
 """
 import Fert_Dataset as fd
import os

loc_Fert = os.getcwd() + r'/Datasets/FertPredictDataset.csv'

dataset = fd.get_fert_dataset(loc_Fert)

X = dataset.iloc[:, :3].values
Y = dataset.iloc[:, 3].values

from sklearn.metrics import confusion_matrix
from sklearn.model_selection import train_test_split

X_train, X_test, Y_train, Y_test = train_test_split(X, Y,
                                                    test_size = 0.2, 
                                                    random_state = 0)

from sklearn.tree import DecisionTreeClassifier
dtree_model = DecisionTreeClassifier(max_depth = 2).fit(X_train, Y_train)

dtree_pred = dtree_model.predict(X_test)
"""