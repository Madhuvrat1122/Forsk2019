# -*- coding: utf-8 -*-
"""
Created on Fri May 31 22:21:23 2019

@author: mv gupta
"""

import pandas as pd  
import numpy as np  
import matplotlib.pyplot as plt  

dataset = pd.read_csv('kc_house_data.csv')  
dataset=dataset.fillna(0)
from sklearn.preprocessing import LabelEncoder
labelencoder = LabelEncoder()
dataset['date']=labelencoder.fit_transform(dataset['date'])
features=dataset.drop("price",axis=1)
labels=dataset['price']
from sklearn.model_selection import train_test_split
features_train, features_test, labels_train, labels_test = train_test_split(features, labels, test_size = 0.25, random_state = 0)
from sklearn.preprocessing import StandardScaler
sc = StandardScaler()
features_train = sc.fit_transform(features_train)
features_test = sc.transform(features_test)
from sklearn.linear_model import LinearRegression  
regressor = LinearRegression()  
regressor.fit(features_train, labels_train)
labels_pred = regressor.predict(features_test) 
df = pd.DataFrame({'Actual': labels_test, 'Predicted': labels_pred})  
print ( df )
#second
from sklearn.linear_model import Lasso
lm_lasso = Lasso() 
lm_lasso.fit(features_train, labels_train)
print ("RSquare Value for Lasso Regresssion TEST data is-")
print (np.round (lm_lasso.score(features_test,labels_test)*100,2))
#third
from sklearn.linear_model import Ridge
lm_ridge =  Ridge()
lm_ridge.fit(features_train, labels_train)
print ("RSquare Value for Ridge Regresssion TEST data is-")
print (np.round (lm_ridge.score(features_test,labels_test)*100,2))