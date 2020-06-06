# -*- coding: utf-8 -*-
"""
Created on Sun Jan 27 15:41:10 2019

@author: Admin
"""
import numpy as np
a = np.matrix('1 2; 3 4')
for i in range(len(a)):
    print(a[i])
    
beta = np.diag([np.deg2rad(5)**2])
print(beta)
c=[np.deg2rad(5)**2]
print(c)
alphas = np.array([0.05**2, 0.005**2, 0.1**2, 0.01**2])
print(alphas)
initial_mean = np.array([180, 50, 0]).reshape((-1, 1))
print(initial_mean[1])
initial_cov = np.diag([10, 10, 1])
print(initial_cov)
print(np.zeros((2,3)))
k=np.zeros((2,3))
print(k[1][1])
print(np.random.seed(2))
x = np.array([[1, 2, 3], [4, 5, 6]])
print(x)
print(np.ravel(x))
x = np.array([[1, 4,6], [9,200,150]])
print(np.ravel(x)[:])
print(np.cos(3.14))
x = np.array([[1, 4,6], [9,200,150]])
print(x)
c=np.array([[1,2,3],[4,5,6],[7,8,9]])
c=c.reshape(1,1,-1)
print(c)
print(np.shape(c))
c=np.array([[1,2,3],[4,5,6],[7,8,9]])
print(c)
c=np.array([[1,2,3],[4,5,6],[7,8,9]])

k=np.array([[2],
            [3],
            [1]])
print(k.shape)
print(np.dot(c,k))
print(c.dot(c))
print(c*c)
print(c.T)
G=np.identity(3)
print(G)