# -*- coding: utf-8 -*-
"""
Created on Mon Jun  3 17:51:34 2019

@author: mv gupta
"""


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn import datasets
#load iris dataset
iris = datasets.load_iris()
features = iris.data  
labels = iris.target
from sklearn.model_selection import train_test_split
features_train, features_test, labels_train, labels_test = train_test_split(features,labels, test_size = 0.3, random_state = 0)
from sklearn.svm import SVC
classifier = SVC(kernel = 'rbf', random_state = 0)
classifier.fit(features_train, labels_train)
labels_pred = classifier.predict(features_test)
from sklearn.metrics import confusion_matrix
cm = confusion_matrix(labels_test, labels_pred)
score = classifier.score(features_test,labels_test)
