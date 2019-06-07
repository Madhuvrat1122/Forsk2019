# -*- coding: utf-8 -*-
"""
Created on Mon May 13 11:18:19 2019

@author: mv gupta
"""
def add(x,y):
    return x+y
from functools import reduce
li1=[]
people = [{'name': 'Mary', 'height': 160},
          {'name': 'Isla', 'height': 80},
          {'name': 'Sam'}]

li=list(filter(lambda x:'height' in x,people))
total=0
for i in li:
    li1.append(i['height'])
total=reduce(add,li1)
print(total/len(li1))
    