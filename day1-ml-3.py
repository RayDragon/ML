# -*- coding: utf-8 -*-
"""
Created on Fri Jun 22 07:45:00 2018

@author: Govind Singh
"""

import pandas as pd

data = pd.read_csv('./train.csv')
data.groupby('Survived')
print('-'*40)
data.groupby(['Sex', 'Survived', 'Pclass'])
print(data)