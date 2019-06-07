# -*- coding: utf-8 -*-
"""
Created on Tue May 14 09:03:04 2019

@author: mv gupta
"""

"""Code Challenge
  Name: 
    Book Shop
  Filename: 
    book_shop2.py
  Problem Statement:
    The same bookshop, but this time we work on a different list.
    
    The sublists of our lists look like this:
    [ordernumber, (article number, quantity, price per unit), 
    ... (article number, quantity, price per unit) ]
       
    [ [1, ("5464", 4, 9.99), ("8274",18,12.99), ("9744", 9, 44.95)], 
      [2, ("5464", 9, 9.99), ("9744", 9, 44.95)],
      [3, ("5464", 9, 9.99), ("88112", 11, 24.99)],
      [4, ("8732", 7, 11.99), ("7733",11,18.99), ("88112", 5, 39.95)] ]
    
   Write a program which returns a list of list with 
    [order number, total amount of order].
    
   Write a Python program, You need to write a solution without using lambda,map,list comprehension first and then with lambda,map,reduce
      
  Hint: 
    use lambda, map and reduce concept to solve the problem  
    from functools import reduce
"""


