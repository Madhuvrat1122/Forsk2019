# -*- coding: utf-8 -*-
"""
Created on Tue May 28 12:21:05 2019

@author: mv gupta
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
dataset = pd.read_csv('bluegills.csv')
#first
#linear nature
features = dataset.iloc[:, :1].values
labels = dataset.iloc[:, 1:].values
from sklearn.linear_model import LinearRegression
regressor = LinearRegression()
regressor.fit(features, labels)
print (regressor.score(features, labels))
#quardetic nature
from sklearn.preprocessing import PolynomialFeatures
poly_object = PolynomialFeatures(degree = 8)
features_poly = poly_object.fit_transform(features)
regressor = LinearRegression()
regressor.fit(features_poly, labels)
print (regressor.score(features_poly, labels))
#second
from sklearn.preprocessing import PolynomialFeatures
poly_object = PolynomialFeatures(degree = 2)
features_poly = poly_object.fit_transform(features)
lin_reg_2 = LinearRegression()
lin_reg_2.fit(features_poly, labels)
print("Predicting result with Polynomial Regression")
x=np.array(5)
x=x.reshape(1,1)
print(lin_reg_2.predict(poly_object.transform(x)))

