# -*- coding: utf-8 -*-
"""
Created on Fri Jun 29 14:24:45 2018

@author: Govind Singh

Given the features of a car we need to predict the class of the car

buying 4-high, 3-high, 2-red, 1-low
maint 4-high, 3-high, 2-red, 1-low
doors 2,3,4,5
persons 2,4,5
lug-bag 1-small, 2mid, 3big
class 

"""
import pandas as pd
import numpy as np
from matplotlib import pyplot as pt
data = pd.read_csv('../DataSets/data.csv')
X = data.iloc[:, :-1].values
Y = data.iloc[:,6].values

from sklearn.preprocessing import LabelEncoder
ssk = LabelEncoder()
Y = ssk.fit_transform(Y)

from sklearn.naive_bayes import GaussianNB
cl = GaussianNB()
cl.fit(X,Y)

ssk.inverse_transform(cl.predict([
        [4,3,2,1,2,3],
        [3,2,4,4,2,3],
        [1,3,2,2,2,3],
        [2,4,5,5,3,1]]))