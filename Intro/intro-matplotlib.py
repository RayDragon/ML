# -*- coding: utf-8 -*-
"""
Created on Thu Jun 21 14:20:51 2018
INTRODUCTION TO MATPLOT LIB
@author: Govind Singh
"""
import matplotlib.pyplot as plt
import numpy as np

arr = np.random.randn(9)
# arr2 = np.random.randn(6)
#plt.plot(arr)
#plt.plot(arr+0.1)
#plt.plot(arr+0.2)
#plt.plot(arr+0.3)
#plot(arr)

# fro line plot(x,y)
# plt.plot(arr,arr+1,'-', c='red', label='Line1')
#plt.plot(1,2,'--', c='red', label='Line2')
'''
plt.legend()
plt.xlabel("X-value")
plt.ylabel("Y-value")
plt.xticks([1,2,3,4,5])
plt.yticks([1,2,3,4,5])
plt.bar([2,3,4],[4,5,6])
plt.title('Bar Graph')

plt.scatter([0,1],[1,4],c='green') #tablue is most popular data visualization tool
'''
p1 = ['c', 'c++', 'java', 'python', 'R', 'Scala']
usage = [10,20,50,80,30, 25]

plt.axis('equal')
# plt.pie(usage, labels=p1, explode=True)
fig = plt.figure()

ax1 = fig.add_subplot(2,2,1)
ax1.plot(np.random.randn(50), c='red')

ax2 = fig.add_subplot(2,2,2)
ax2.plot(np.random.randn(50), c='blue')

ax3 = fig.add_subplot(2,2,3)
ax3.plot(np.random.randn(50), c='green')

ax4 = fig.add_subplot(2,2,3)
ax4.plot(np.random.randn(50), c='black')



plt.show()
