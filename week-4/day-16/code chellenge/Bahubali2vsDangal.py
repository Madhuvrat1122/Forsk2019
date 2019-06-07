# -*- coding: utf-8 -*-
"""
Created on Mon May 27 12:31:54 2019

@author: mv gupta
"""

import pandas as pd  
import numpy as np  
import matplotlib.pyplot as plt  
dataset = pd.read_csv('Bahubali2_vs_Dangal.csv')
features = dataset.iloc[:, :1].values
labels = dataset.iloc[:,1:].values