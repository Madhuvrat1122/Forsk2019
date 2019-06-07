# -*- coding: utf-8 -*-
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

dataset = pd.read_csv("breast_cancer.csv")
dataset['G']=dataset['G'].fillna(dataset['G'].value_counts().idxmax())
#first solution
features=dataset.drop(["A","K"],axis=1)
labels=dataset['K']
def check(data):
    if data==4:
        return 'y'
    else:
        return 'F'
from sklearn.model_selection import train_test_split
features_train, features_test, labels_train, labels_test = train_test_split(features, labels, test_size = 0.3, random_state = 0)
labels_train=labels_train.apply(check)
labels_test=labels_test.apply(check)
from sklearn.svm import SVC
classifier = SVC(kernel = 'rbf', random_state = 0)
classifier.fit(features_train, labels_train)

# Predicting the Test set results
labels_pred = classifier.predict(features_test)
    
print(pd.DataFrame({'Actual':labels_test, 'Predicted':labels_pred}))
# Making the Confusion Matrix
from sklearn.metrics import confusion_matrix
cm = confusion_matrix(labels_test, labels_pred)

# Model Score
score = classifier.score(features_test,labels_test)

#second solution
dataset = pd.read_csv("breast_cancer.csv")
dataset['G']=dataset['G'].fillna(dataset['G'].value_counts().idxmax())
features=dataset.drop(["A","K"],axis=1)
labels=dataset['K']
def check1(data):
    if data==4:
        return 'Malignant'
    else:
        return 'Benign'
from sklearn.model_selection import train_test_split
features_train, features_test, labels_train, labels_test = train_test_split(features, labels, test_size = 0.3, random_state = 0)
labels_train=labels_train.apply(check1)
labels_test=labels_test.apply(check1)
from sklearn.svm import SVC
classifier = SVC(kernel = 'rbf', random_state = 0)
classifier.fit(features_train, labels_train) 
list1=np.array([6,2,5,3,2,7,9,2,4])
list1=list1.reshape(1,-1)
print(classifier.predict(list1))