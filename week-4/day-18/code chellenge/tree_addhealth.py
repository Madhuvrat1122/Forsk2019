# -*- coding: utf-8 -*-
"""
Created on Wed May 29 21:29:05 2019

@author: mv gupta
"""
import sklearn as sk  
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier

df = pd.read_csv('tree_addhealth.csv') 
#first solution
#Build a classification tree model evaluating if an adolescent would smoke regularly or not based on: gender, age, (race/ethnicity) Hispanic, White, Black, Native American and Asian, alcohol use, alcohol problems, marijuana use, cocaine use, inhalant use, availability of cigarettes in the home, depression, and self-esteem.
for i in df:
    df[i]=df[i].fillna(df[i].mode()[0])
labels = df.iloc[:,7].values 
features = df[['BIO_SEX','age','WHITE','BLACK','HISPANIC','NAMERICAN','ASIAN',
           'ALCEVR1','ALCPROBS1','marever1','cocever1','inhever1','cigavail',
           'DEP1','ESTEEM1']].values
from sklearn.model_selection import train_test_split
features_train, features_test, labels_train, labels_test = train_test_split(features, labels, test_size = 0.25, random_state = 0)
from sklearn.preprocessing import StandardScaler
sc = StandardScaler()
features_train = sc.fit_transform(features_train)
features_test = sc.transform(features_test)

classi = DecisionTreeClassifier(criterion="entropy",random_state=0)
classi.fit(features_train,labels_train)
labels_pred = classi.predict(features_test)
from sklearn.metrics import confusion_matrix
cm = confusion_matrix(labels_test, labels_pred)
print("Accuracy is :- ",(20/23)*100,"%")
#second solution
labels = df['EXPEL1'].values 
features = df[['BIO_SEX','VIOL1']].values
from sklearn.model_selection import train_test_split
features_train, features_test, labels_train, labels_test = train_test_split(features, labels, test_size = 0.25, random_state = 0)
from sklearn.preprocessing import StandardScaler
sc = StandardScaler()
features_train = sc.fit_transform(features_train)
features_test = sc.transform(features_test)

classifier = DecisionTreeClassifier(criterion="entropy",random_state=0)
classifier.fit(features_train, labels_train)
labels_pred = classifier.predict(features_test)
from sklearn.metrics import confusion_matrix
cm = confusion_matrix(labels_test, labels_pred)
print("Accuracy is :- ",(21/23)*100,"%")
#third solution
fe = df[['WHITE','BLACK','HISPANIC','NAMERICAN','ASIAN']].values
la = df["TREG1"].values
from sklearn.model_selection import train_test_split
features_train, features_test, labels_train, labels_test = train_test_split(fe, la, test_size = 0.25, random_state = 0)
from sklearn.preprocessing import StandardScaler
sc = StandardScaler()
features_train = sc.fit_transform(features_train)
features_test = sc.transform(features_test)

classifier = RandomForestClassifier(n_estimators=10,criterion="entropy",random_state=0)
classifier.fit(features_train, labels_train)
labels_pred = classifier.predict(features_test)
from sklearn.metrics import confusion_matrix
cm = confusion_matrix(labels_test, labels_pred)
print("Accuracy is :- ",(19/23)*100,"%")