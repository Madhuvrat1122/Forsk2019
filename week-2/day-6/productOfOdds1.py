# -*- coding: utf-8 -*-
"""
Created on Mon May 13 13:23:23 2019

@author: mv gupta
"""


li=[int(i) for i in input().split()]
result=reduce(lambda x,y:x*y,list(filter(lambda x: x%2==1,li)))
print(result)
