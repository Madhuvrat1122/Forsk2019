# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import numpy as np
import pandas as pd
import statsmodels.api as sm
import matplotlib.pyplot as plt
dataset = pd.read_csv('Female_Stats.csv')
features = dataset.iloc[:, 1:].values
labels = dataset.iloc[:, 0].values
#first model
features = sm.add_constant(features)
features_opt = features[:, [0, 1, 2]]
regressor_OLS = sm.OLS(endog = labels, exog = features_opt).fit()
regressor_OLS.summary()

#second model
#when father height is constant
from sklearn.linear_model import LinearRegression
regressor = LinearRegression()
features = dataset.iloc[:,1:].values
labels = dataset.iloc[:, :1].values
regressor.fit(features, labels) 
print (regressor.coef_)



























