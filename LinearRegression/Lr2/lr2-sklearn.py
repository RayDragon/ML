# -*- coding: utf-8 -*-
"""
Created on Tue Jun 26 18:28:59 2018

@author: Govind Singh
"""

import pandas as pd
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as pt

data = pd.read_csv('lr2-sklearn.csv')
data = data.loc[:16] # removing null parametered values

# removing $ and , from price
for i in range(len(data['Median home price'])):
    # here $123,456 will be made as variable = '123' + '456' all all the money is 6 digit 
    data['Median home price'][i] = float(data['Median home price'][i][1:4]+data['Median home price'][i][5:])
''' 
since X needs wo be in the form 
X = [
     [1],
     [2],
     [3],
     .
     .
     .
] i,e, 2-d array
and y in the form
Y = [
         1,
         2,
         3,
         4
         .
         .
         
    ] i.e. simple 1-d array
'''
X = data.loc[:16, ['interest rate (%)']].values
# pd.numeric will convert string to float value therefore
Y = data.loc[:16, 'Median home price'].values

lr = LinearRegression()
lr.fit(X, Y)

lr.predict(10)

# Now to make graph
## The actual data
pt.scatter(X, Y, c='red')
## Now the regression line with min and max value
pt.plot([6,10],lr.predict([[6],[10]]), c='blue')
