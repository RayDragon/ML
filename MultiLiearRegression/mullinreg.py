# -*- coding: utf-8 -*-
import pandas as pd
from sklearn.preprocessing import LabelEncoder, OneHotEncoder
from sklearn.cross_validation import train_test_split
from sklearn.linear_model import LinearRegression
from matplotlib import pyplot as pt

data = pd.read_csv('50_Startups.csv')

X = data.iloc[:, :-1].values
Y = data.iloc[:, 4].values

labelencoder = LabelEncoder()
X[:,3]=labelencoder.fit_transform(X[:,3])
ohe = OneHotEncoder(categorical_features=[3])
X = ohe.fit_transform(X).toarray()
X = X[:, 1:]

xtrain,xtest,ytrain,ytest = train_test_split(X, Y, test_size=1/3, random_state=0)

lr = LinearRegression()
lr.fit(xtrain, ytrain)

ypredict = lr.predict(xtest)

for i in range(5):
    pt.scatter(xtest[:, i], ytest, c='red')
    pt.scatter(xtest[:, i], ypredict,c='blue')
    pt.show()

# Building the optial model using backward elimination
import statsmodels.formula.api as sm
import numpy as np

X = np.append(arr=np.ones((50, 1)).astype(int), values=X, axis=1)


X_opt = X[:, [0,3]]
regressor_OLS = sm.OLS(endog=Y, exog=X_opt).fit()
regressor_OLS.summary()
