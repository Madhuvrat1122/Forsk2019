# -*- coding: utf-8 -*-
"""
Created on Wed May 29 11:01:50 2019

@author: mv gupta
"""

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
dataset = pd.read_csv('affairs.csv')
features = dataset.iloc[:, :-1].values
labels = dataset.iloc[:, -1].values
from sklearn.preprocessing import OneHotEncoder
onehotencoder = OneHotEncoder(categorical_features = [6,7])
features = onehotencoder.fit_transform(features).toarray()
# Feature Scaling
from sklearn.preprocessing import StandardScaler
sc = StandardScaler()
features = sc.fit_transform(features)
from sklearn.model_selection import train_test_split
features_train, features_test, labels_train, labels_test = train_test_split(features, labels, test_size = 0.25, random_state = 40)

#logistic regression
from sklearn.linear_model import LogisticRegression
classifier = LogisticRegression()
classifier.fit(features_train, labels_train)
#Calculate Class Probabilities
probability = classifier.predict_proba(features_test)
# Predicting the class labels
labels_pred = classifier.predict(features_test)
# Making the Confusion Matrix
from sklearn.metrics import confusion_matrix
cm = confusion_matrix(labels_test, labels_pred)
print("Accuracy is:- {}".format((972+169)/1592))
print("Accuracy is:- {}".format(classifier.score(features_test,labels_test)))
print("Woman having affairs:- {}".format((169+334)/1592))
# Predict the probability of an affair for a random woman not present in the dataset. She's a 25-year-old teacher who graduated college, has been married for 3 years, has 1 child, rates herself as strongly religious, rates her marriage as fair, and her husband is a farmer.
from sklearn.linear_model import LinearRegression  
regressor = LinearRegression()  
x=[4,25,3,1,4,16,4,2]
x=np.array(x)
x=x.reshape(1,8)
x_hot = onehotencoder.transform(x).toarray()
x_fit = sc.transform(x_hot)
print("Score:- ",classifier.predict(x_fit))