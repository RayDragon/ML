# -*- coding: utf-8 -*-
'''
This program will check the majority of life and death
'''
import pandas as pd

data = pd.DataFrame(pd.read_csv('train.csv'))
print('Survived:',data.loc[data.Survived==1]['Survived'].count())
print('Died:',data.loc[data.Survived==0]['Survived'].count())


'''
The result shows that the people who survived are lesser than those who dies 
so as a wild guess, say for any passengerId, make its survival to 0
we get
'''

data2 = pd.read_csv('test.csv')
data2['Survived'] = 0
data2.loc[data2.Sex=='female', 'Survived'] = 1
#Saving the file
#data2[:, ['PassengerId', 'Survived']].to_csv('result_all_died.csv', index=False)


