# -*- coding: utf-8 -*-
"""
Created on Thu Jun 28 09:48:41 2018

@author: Govind Singh
"""

import pandas as pd
from matplotlib import pyplot as pt
import numpy as np

data = pd.read_csv('Position_Salaries.csv')

X = data.iloc[:, 1:2].values
Y = data.iloc[:, 2].values

from sklearn.tree import DecisionTreeRegressor

dsreg = DecisionTreeRegressor(random_state=0)
dsreg.fit(X,Y)
dsreg.predict([[1],[2],[3],[4],[5]])

xtest = np.linspace(0,12, 100,endpoint=True)
xtest.resize(100,1)

pt.figure(figsize=(15,5))
pt.xticks(np.arange(0,12,0.5))
pt.plot(xtest, dsreg.predict(xtest))
pt.scatter(X,Y,c='red')



'''
7-July (Phase 2)
DLF Epitrem
Tower B
(Hour -10)

twitter CodeWithSimon
@techno_simon (twittor)
@me_stephen_simon (insta)
'''