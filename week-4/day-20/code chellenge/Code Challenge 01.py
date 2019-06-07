# -*- coding: utf-8 -*-
"""
Created on Fri May 31 10:49:02 2019

@author: mv gupta
"""

import pandas as pd  
import numpy as np  
import matplotlib.pyplot as plt  
url = 'http://www.stat.cmu.edu/~ryantibs/statcomp/data/pros.dat'
dataset = pd.read_csv(url,delim_whitespace=True)
#last solution(b)
def dataset1(value):
    if value>4.0:
        value='H'
    else:
        value='L'
    return value
dataset['lpsa']=dataset['lpsa'].apply(dataset1)

features=dataset.drop('lpsa',axis=1)
labels=dataset['lpsa']
from sklearn.preprocessing import LabelEncoder
labelencoder = LabelEncoder()
labels=labelencoder.fit_transform(labels)
from sklearn.model_selection import train_test_split  
features_train, features_test, labels_train, labels_test = train_test_split(features, labels, test_size=0.2, random_state=0)
from sklearn.tree import DecisionTreeClassifier  
classifier = DecisionTreeClassifier()  
classifier.fit(features_train, labels_train)
labels_pred = classifier.predict(features_test) 
print(pd.DataFrame({'Actual': labelencoder.inverse_transform(labels_test),'Predicted':labelencoder.inverse_transform(labels_pred)}))
print("Accuracy:- ",classifier.score(features_test,labels_test)*100,"%")
#first solution
#(a).(1)
import pandas as pd  
import numpy as np  
import matplotlib.pyplot as plt  
url = 'http://www.stat.cmu.edu/~ryantibs/statcomp/data/pros.dat'
dataset = pd.read_csv(url,delim_whitespace=True)
features = dataset.iloc[:, :-1].values  
labels = dataset.iloc[:, -1].values
from sklearn.model_selection import train_test_split  
features_train, features_test, labels_train, labels_test = train_test_split(features, labels, test_size=0.2, random_state=0)  
from sklearn.linear_model import LinearRegression  
regressor = LinearRegression()  
regressor.fit(features_train, labels_train) 
labels_pred = regressor.predict(features_test) 
df = pd.DataFrame({'Actual': labels_test, 'Predicted': labels_pred})  
print ( df )
import numpy as np
from sklearn import metrics
print ("Simple Regression Mean Square Error (MSE) for TEST data is") 
print (np.round (metrics .mean_squared_error(labels_test, labels_pred),2) )
#(a).(2)
from sklearn.linear_model import Lasso
from sklearn.linear_model import Ridge
from sklearn.linear_model import ElasticNet
lm_lasso = Lasso() 
lm_ridge =  Ridge() 
lm_elastic = ElasticNet() 
lm_lasso.fit(features_train, labels_train)
lm_ridge.fit(features_train, labels_train)
lm_elastic.fit(features_train, labels_train)
print ("RSquare Value for Lasso Regresssion TEST data is-")
print (np.round (lm_lasso.score(features_test,labels_test)*100,2))

print ("RSquare Value for Ridge Regresssion TEST data is-")
print (np.round (lm_ridge.score(features_test,labels_test)*100,2))

print ("RSquare Value for Elastic Net Regresssion TEST data is-")
print (np.round (lm_elastic.score(features_test,labels_test)*100,2))