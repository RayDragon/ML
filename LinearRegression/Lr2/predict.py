# -*- coding: utf-8 -*-
"""
Created on Tue Jun 26 14:35:50 2018

@author: Govind Singh
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as pt
from sklearn.linear_model import LinearRegression

# Read the data file as is
data =pd.read_csv('./Sample-data-sets-for-linear-regression2.csv')

# Get a glimps of it
print(data.head())

# Getting the x parameters (in numeric datatype)
X = pd.to_numeric( data['X VARIABLE'].loc[1:17].values)
Y = data['Y VARIABLE'].loc[1:17].values # Y parameter in string type

# Removing $ and , from the ammount value
for i in range(len(Y)):
    Y[i] = Y[i][1:4]+Y[i][5:]

# Converting string values stored in Y to numeric
Y = pd.to_numeric(Y)

# Getting the mean values
x_mean, y_mean = X.mean(), Y.mean()

# Numerator and denominator...
num,den=0,0
for i in range(len(X)):
    num += (X[i]-x_mean)*(Y[i]-y_mean)
    den += (X[i]-x_mean)**2

# Taking the value for b1 and b0
b1 = num/den
b0 = y_mean-b1*x_mean

# Now we get our regression line as y = b0 + b1 * X
def y(x):
    return b0 + b1*x

# Now to predict 10 lets call the function like this
y(10)    

# Plotting the trained date set graph
pt.scatter(X, Y, c='blue')

# Plotting the regression line (with the min and max x values and their 
# predicted i.e. y(x) value)
pt.plot([5,10], [y(5), y(10)], c='red')
pt.show()