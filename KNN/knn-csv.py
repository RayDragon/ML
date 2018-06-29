# -*- coding: utf-8 -*-
"""
Created on Fri Jun 29 15:28:33 2018

@author: Govind Singh
"""

import pandas as pd


data = pd.read_csv('../DataSets/knn.csv')

X = data.iloc[:, 0:4].values
Y = data.iloc[:, 4].values

from sklearn.preprocessing import LabelEncoder
enc = LabelEncoder()
Y = enc.fit_transform(Y)

from sklearn.neighbors import KNeighborsClassifier
cl = KNeighborsClassifier(n_neighbors=5, p=2)

cl.fit(X,Y)
enc.inverse_transform(cl.predict([5,3,1,0]))