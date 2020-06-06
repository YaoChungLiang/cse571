# -*- coding: utf-8 -*-
"""
Created on Thu Feb 28 13:50:47 2019

@author: Admin
"""
#import tensorflow as tf
import numpy as np
import numpy
import math
a=[2, 1, -2, -1, -2, 1, -1, 1, -1, -2]
AUCG_list=[]
AUCG_string=''
for i in a:
    if i == 2 :
        AUCG_list.append('C')
    elif i == -2:
        AUCG_list.append('G')
    elif i == 1:
        AUCG_list.append('A')
    elif i == -1:
        AUCG_list.append('U')
    else:
        pass
print(AUCG_list)
AUCG_string=AUCG_string.join(AUCG_list)
print(AUCG_string)
        
#def dist(a,b):
#    return np.sqrt((a[0]-b[0])**2+(a[1]-b[1])**2)
#start=[13,13]
#plan=[[3,4],[7,8],[11,11],[20,30],[1000,1000],[100,100],[5,7]]
#dists=[]
#cost=[0]*len(plan)
#reversed_edge={1:2,3:4,4:5,5:6,0:1,2:3}
#edge={value:key for key,value in reversed_edge.items() }
#print(edge)
#for key,value in reversed_edge.items():
#    print(key)
#    cost[reversed_edge[key]]=cost[key]+dist(plan[key],plan[value])
#print(cost)

            
#for i in range(len(plan)):
#    print(plan[i])
#    print(i)
#for i in range(len(plan)):
#    dists+=[dist(plan[i],start)]
#dists = numpy.array(dists)
#print(dists)
#knnIDs = numpy.argpartition(dists, 6)
#print(knnIDs)
#plan=np.array(plan)
#print(plan[knnIDs])
#print(plan[knnIDs][:10])
#
#plan=plan.tolist()
#print(plan)