# -*- coding: utf-8 -*-
"""
Created on Mon May 13 10:24:21 2019

@author: mv gupta
"""
li=[]
s =[int(i) for i in input().split(' ')]
for i in s:
    temp=i
    Reverse = 0    
    while(i > 0):    
        Reminder = i %10    
        Reverse = (Reverse *10) + Reminder    
        i = i //10  
    if temp==Reverse:
        li.append(True)
    else:
        li.append(False)
       
print(all(li))
    


    

    
            
            
