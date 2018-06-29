# -*- coding: utf-8 -*-
import pandas as pd
from matplotlib import pyplot as pt
import numpy as np
data = pd.read_csv('Position_Salaries.csv')
X = data.iloc[:, 1:2].values
Y = data.iloc[:, 2].values

from sklearn.preprocessing import PolynomialFeatures
poly_reg = PolynomialFeatures(degree=5)

X_poly = poly_reg.fit_transform(X)
poly_reg.fit(X_poly, Y)


from sklearn.linear_model import LinearRegression
lr = LinearRegression()
lr.fit(X_poly, Y)
var = np.linspace(0,10,50).reshape(50,1)
sol = lr.predict(poly_reg.fit_transform(var))

pt.plot(var,sol, c='blue')
pt.scatter(X,Y, c='red')

lr.predict(poly_reg.fit_transform(10.5))
