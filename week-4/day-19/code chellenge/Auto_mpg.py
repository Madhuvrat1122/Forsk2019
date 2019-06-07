# -*- coding: utf-8 -*-
"""
Created on Thu May 30 09:24:29 2019

@author: mv gupta
"""
import pandas as pd  
import numpy as np  
import matplotlib.pyplot as plt 
data = pd.read_fwf('Auto_mpg.txt',header=None)
data.columns=["mpg", "cylinders", "displacement","horsepower","weight","acceleration", "model year", "origin", "car name"]
data['horsepower']=data['horsepower'].replace({"?":0}) 
#first solution
print(data[data['mpg']==data['mpg'].max()]['car name'].values[0])
#secong solution
#by decison tree
features = data.drop(['mpg','car name'],axis=1)
labels = data['mpg']  

from sklearn.model_selection import train_test_split  
features_train, features_test, labels_train, labels_test = train_test_split(features, labels, test_size=0.2, random_state=0) 

from sklearn.tree import DecisionTreeRegressor  
regressor = DecisionTreeRegressor()  
regressor.fit(features_train, labels_train)

labels_pred = regressor.predict(features_test)
df=pd.DataFrame({'Actual':labels_test, 'Predicted':labels_pred})  
print("Accuracy:- ",regressor.score(features_test,labels_test))
 #random forest
from sklearn.preprocessing import StandardScaler
sc = StandardScaler()  
features_train = sc.fit_transform(features_train)  
features_test = sc.transform(features_test)  
from sklearn.ensemble import RandomForestRegressor
regressor = RandomForestRegressor(n_estimators=25, random_state=0)  
regressor.fit(features_train, labels_train)  
labels_pred = regressor.predict(features_test)   
print("Accuracy:- ",regressor.score(features_test,labels_test))
#third solution
list1=np.array([6,215,100,2630,22.2,80,3])
list1=list1.reshape(1,-1)
print(regressor.predict(list1))