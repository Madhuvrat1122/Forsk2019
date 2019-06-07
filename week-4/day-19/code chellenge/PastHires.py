# -*- coding: utf-8 -*-
"""
Created on Thu May 30 11:46:56 2019

@author: mv gupta
"""

import pandas as pd  
import numpy as np  
dataset = pd.read_csv('PastHires.csv') 
from sklearn.preprocessing import LabelEncoder
labelencoder = LabelEncoder()
dataset['Employed?'] = labelencoder.fit_transform(dataset['Employed?'])
dataset['Level of Education']=labelencoder.fit_transform(dataset['Level of Education'])
dataset['Top-tier school']=labelencoder.fit_transform(dataset['Top-tier school'])
dataset['Interned']=labelencoder.fit_transform(dataset['Interned'])
dataset['Hired']=labelencoder.fit_transform(dataset['Hired'])
#first solution
features = dataset.iloc[:,:-1]
labels = dataset['Hired']  
from sklearn.model_selection import train_test_split  
features_train, features_test, labels_train, labels_test = train_test_split(features, labels, test_size=0.50)  
from sklearn.tree import DecisionTreeClassifier  
classifier = DecisionTreeClassifier()  
classifier.fit(features_train, labels_train)
labels_pred = classifier.predict(features_test) 
print(pd.DataFrame({'Actual': labelencoder.inverse_transform(labels_test),'Predicted':labelencoder.inverse_transform(labels_pred)}))
print("Accuracy:- ",classifier.score(features_test,labels_test))
#second solution
dataset = pd.read_csv("PastHires.csv")    
from sklearn.preprocessing import LabelEncoder
labelencoder = LabelEncoder()
features = dataset.iloc[:,:-1]
labels = dataset['Hired']
from sklearn.model_selection import train_test_split
features_train, features_test, labels_train, labels_test = train_test_split(features, labels, test_size=0.2, random_state=0)
from sklearn.ensemble import RandomForestClassifier
classifier = RandomForestClassifier(n_estimators=20, random_state=0)  
classifier.fit(features_train, labels_train)
list1=np.array([10,'Y',4,'BS','Y','N'])
list1=list1.reshape(1,6)
list1[:,1]=labelencoder.fit_transform(list1[:,1])
list1[:,3]=labelencoder.fit_transform(list1[:,3])
list1[:,4]=labelencoder.fit_transform(list1[:,4])
list1[:,5]=labelencoder.fit_transform(list1[:,5])
print(labelencoder.inverse_transform(classifier.predict(list1)))
#next part of second
list1=np.array([10,'N',4,'BMS','Y','Y'])
list1=list1.reshape(1,6)
list1[:,1]=labelencoder.fit_transform(list1[:,1])
list1[:,3]=labelencoder.fit_transform(list1[:,3])
list1[:,4]=labelencoder.fit_transform(list1[:,4])
list1[:,5]=labelencoder.fit_transform(list1[:,5])
print(labelencoder.inverse_transform(classifier.predict(list1)))



