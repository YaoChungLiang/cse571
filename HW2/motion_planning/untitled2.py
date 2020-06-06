# -*- coding: utf-8 -*-
"""
Created on Thu Feb 28 01:11:02 2019

@author: yaochungliang
"""

class tree:
    def __init__(self,data):
        self.child={}
        self.data=data
    def insert(self,id,data):
        self.child[id]=data
KKK=tree(3)
KKK.insert(0,"GG")
print(KKK.child)
for i in range(10):
    j=i+10
    KKK.insert(i,j)
print(KKK.child)