# -*- coding: utf-8 -*-
"""
Created on Wed May 29 12:52:40 2019

@author: mv gupta
"""

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
dataset = pd.read_csv('mushrooms.csv')
dummy=pd.get_dummies(dataset.iloc[:,[0,5,21,22]])
features = dummy.iloc[:, 2:].values
labels = dummy.iloc[:, :1].values
from sklearn.model_selection import train_test_split
features_train, features_test, labels_train, labels_test = train_test_split(features, labels, test_size = 0.25, random_state = 40)
from sklearn.linear_model import LogisticRegression
classifier = LogisticRegression()
classifier.fit(features_train, labels_train)
print("Score:- ",classifier.score(features_test,labels_test))