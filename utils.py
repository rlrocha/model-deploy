# -*- coding: utf-8 -*-
"""
Created on Sat Oct 16 21:32:29 2021

@author: Rafael Rocha
"""

import numpy as np
from sklearn.linear_model import LinearRegression

def predictions(X_test):
    
    X = np.arange(1, 1001)
    y = np.sqrt(X)
    
    X = X.reshape(-1, 1)
    y = y.reshape(-1, 1)
    
    model = LinearRegression()
    model.fit(X, y)
    
    X_test = np.array(X_test)
    X_test = X_test.reshape(-1, 1)
    
    X_pred = model.predict(X_test)[0]
    
    return X_pred