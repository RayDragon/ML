# -*- coding: utf-8 -*-
"""
Created on Fri Jun 22 04:34:03 2018

@author: Govind Singh
"""

import pandas as pd

dataset = pd.read_csv('./test.csv')
print(dataset)
dataset['Survived']=0
#dataset.to_csv('./res.csv', columnsqwqw`dfdsavcxz=['PassengerId','Survived'], index=False)
# print(dataset.Sex)
print('-')
i=0
'''for x in dataset.Sex:
    if x == 'female':
        dataset.Survived[i]=0
    i+=1'''
print(dataset.columns)
'''
for i in range(0,len(dataset.Sex)):
    if dataset.Sex[i]=='female':
        dataset.Survived[i]=1
print(dataset.Survived)
'''
dataset.loc[dataset.Sex=='female', 'Survived']=1 
dataset.to_csv('./gender.csv', columns=['PassengerId', 'Survived'], index=False)
print('file saved')