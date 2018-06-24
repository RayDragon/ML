# -*- coding: utf-8 -*-
"""
Created on Sun Jun 24 16:53:37 2018

@author: Govind Singh
"""
import pandas as pd

data = pd.read_csv('train.csv')

male = data.loc[data.Sex=='male']
female = data.loc[data.Sex=='female']

def fprint(*args):
    for arg in args:
        print(arg, end='\t\t')
    print()

ms, md = male.loc[male.Survived==1]['Survived'].count(), male.loc[male.Survived==0]['Survived'].count()
fms, fmd = female.loc[female.Survived==1]['Survived'].count(), female.loc[female.Survived==0]['Survived'].count()

fprint('Gender','Survived','Died','S/D :')
fprint('male', ms,md, float(ms)/float(md))
fprint('female', fms, fmd, float(fms)/float(fmd))


'''
This above data shows that if a case is of male, most likely he died
while for female, they survived
so as a wild guess, if the new passenger is female, most likely
she had survived so
'''

data2 = pd.read_csv('test.csv')
data2['Survived']=0
data2.loc[data2.Sex=='female', 'Survived']=1
data2.loc[:, ['PassengerId', 'Survived']].to_csv('result_females_survived.csv', index=False)
