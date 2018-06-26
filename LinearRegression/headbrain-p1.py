# -*- coding: utf-8 -*-
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv('headbrain.csv')

print(data.head())

#collecting x and y
X = data['Head Size(cm^3)']
Y = data['Brain Weight(grams)']

#MEan of x and y
mean_x = np.mean(X)
mean_y = np.mean(Y)

# Total number of values
m = len(X)

num = 0
den = 0

for i in range(m):
    num += (X[i]-mean_x)*(Y[i]-mean_y)
    den += (X[i]-mean_x)**2
    
b1 = num/den
b0 = mean_y - b1*mean_x

#Print coefficients
print(b1,b0)

# got the predictor
def y(x):
    return b0 + b1*x

#plotting the graph of x and y
plt.scatter(X, Y)
plt.plot([2750, 4750], [y(2750), y(4750)], c='red')
plt.show()

'''
This is very good for small dataset, however when the dataset is very big,
this will cause a huge burden to server
so we use scikit learn which does this at lower level for us
'''


