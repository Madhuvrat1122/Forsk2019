# -*- coding: utf-8 -*-
"""
Created on Thu Jun  6 11:08:31 2019

@author: mv gupta
"""

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.cluster import KMeans
# Importing the dataset
#first task
dataset = pd.read_csv('data.csv')
print(dataset['Country'].value_counts())
#second task
print(dataset['Classification'].value_counts().head(2))
#third task
print(dataset['Artist Role'].value_counts())
#fourth task
print(dataset['Culture'].value_counts().head(2))
