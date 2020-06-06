# -*- coding: utf-8 -*-
"""
Created on Wed Feb 27 23:24:46 2019

@author: Admin
"""
from matplotlib import pyplot as plt
import numpy as np
import numpy
mapfile='map1.txt'
mymap=np.loadtxt(mapfile)
print(mymap)
for i in range(numpy.shape(mymap)[0] - 1):
    for j in range(numpy.shape(mymap)[1] - 1):
        x = [mymap[i,0], mymap[i+1, 0]]
        y = [mymap[j,1], mymap[j+1, 1]]
        plt.plot(y, x, 'b')
#plt.show()
#plt.show(mymap)