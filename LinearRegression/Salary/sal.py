# -*- coding: utf-8 -*-

import numpy as np
import pandas as pd
import matplotlib.pyplot as pyt
from sklearn.cross_validation import train_test_split
from sklearn.linear_model import LinearRegression

data = pd.read_csv('Salary_Data.csv')

#X, Y = data['YearsExperience'], data['Salary']
X = data.iloc[:, :-1].values
Y = data.iloc[:, 1].values
# mean_x , mean_y = X.mean(), Y.mean()
'''
X_train = data.iloc[0:-10, 0].values
Y_train = data.iloc[0:-10, 1].values
X_test = data.iloc[-10:, 0].values
Y_test = data.iloc[-10:, 1].values
 '''
x_train, x_test, y_train, y_test = train_test_split(X,Y, test_size=1.0/3.0, random_state=10 )

regressor = LinearRegression()
regressor.fit(x_train, y_train)


Y_predict=regressor.predict(x_test)

pyt.scatter(x_test, y_test)
pyt.scatter(x_test, Y_predict)
pyt.legend(['test', 'predict'])
pyt.show()
#print(Y)
