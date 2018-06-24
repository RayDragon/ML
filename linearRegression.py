# -*- coding: utf-8 -*-
"""
Created on Fri Jun 22 10:03:01 2018

@author: Govind Singh
"""

import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression

data = pd.read_csv('./linearrigression.csv', delim_whitespace=True)

print(data.head())

x_train = data['Father'].values[:, np.newaxis]
y_train = data['Son'].values

lr = LinearRegression()

lr.fit(x_train, y_train)
print(lr.predict(100))
