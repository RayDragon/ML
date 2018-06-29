# -*- coding: utf-8 -*-
"""
Created on Thu Jun 28 12:06:26 2018

@author: Govind Singh
"""

import pandas as pd
import numpy as np

data = pd.read_csv('../Datasets/Social_Network_Ads.csv')

X = data.iloc[:, 2:3].values
Y = data.iloc[:, 4].values

#Just splitting data
X_train, X_test = X[:300, :], X[300:, :]
Y_train, Y_test = Y[:300], Y[300:]

#plotting data 
from matplotlib import pyplot as pt
pt.scatter(X,Y)
pt.show()

# Fill empty values
'''
from sklearn.preprocessing import StandardScaler
sc = StandardScaler()
X_train = sc.fit_transform(X_train)
Y_test = sc.fit_transform(Y_test)
'''

from sklearn.linear_model import LogisticRegression
classifier = LogisticRegression(random_state=0)

classifier.fit(X_train,Y_train)
y_predict = classifier.predict(X_test)
y_prob = classifier.predict_proba(X_test)

pt.yticks([0,1])
pt.scatter(X_test, y_predict+0.2, c='blue')
pt.scatter(X_test, Y_test, c='red')
pt.plot(X_test, y_prob, c='green')

classifier.get_params()

# Making a confusion matrix
from sklearn.metrics import confusion_matrix
cm = confusion_matrix(Y_test, y_predict)
pt.plot(cm)

## -------------------
