# -*- coding: utf-8 -*-
"""
Created on Mon May 13 11:02:57 2019

@author: mv gupta
"""
import random
names = ['Mary', 'Isla', 'Sam']
code_names = ['Mr. Pink', 'Mr. Orange', 'Mr. Blonde']
secret_name=list(map(lambda x:random.choice(code_names),names))
print(secret_name)

