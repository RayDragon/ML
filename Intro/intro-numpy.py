# -*- coding: utf-8 -*-
"""
Created on Thu Jun 21 12:03:22 2018

@author: Govind Singh
"""
import numpy as np
data = [
        [1,2,3,4],
        [5,6,7,8]
        ]
data = np.array(data)
print(data,'\n', data-2,'\n', data*data)
print(np.zeros((2,5)), '\n', data.reshape((4,2)), '\n', data.T)
print('------------'*5)
x = np.random.randn(5)
print(x)
print(x.mean(), x)

X = np.matrix(x)
print(X)
y=X+2
print(y)
