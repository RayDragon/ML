# -*- coding: utf-8 -*-
"""
Created on Sun Jun 24 08:17:26 2018

@author: Govind Singh
This is made to display the data present in train model 'train.csv' 
"""
import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv('train.csv')
data = pd.DataFrame(data)
#print(data.head())
data2 = data.loc[data.Sex == 'female'].loc[data.Survived==0, ['Sex', 'Survived']]
print(data2)


print( )
