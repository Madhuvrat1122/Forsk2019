# -*- coding: utf-8 -*-
"""
Created on Mon May 27 12:01:18 2019

@author: mv gupta
"""
import pandas as pd  
import numpy as np  
import matplotlib.pyplot as plt 

dataset = pd.read_csv('Foodtruck.csv')  
plt.boxplot(dataset.values)
dataset.plot(x='Population', y='Profit', style='o')  
plt.title('Hours vs Percentage')  
plt.xlabel('Hours Studied')  
plt.ylabel('Percentage Score')  
plt.show()
features = dataset.iloc[:, :-1].values  
labels = dataset.iloc[:, 1].values 
from sklearn.linear_model import LinearRegression  
regressor = LinearRegression()  
regressor.fit(features, labels)
print(regressor.intercept_)  
print(regressor.coef_)
x=np.array(3.073)
x=x.reshape(1,1)
print(regressor.predict(x))