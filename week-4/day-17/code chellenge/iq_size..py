# -*- coding: utf-8 -*-
"""
Created on Tue May 28 12:53:05 2019

@author: mv gupta
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
dataset = pd.read_csv('iq_size.csv')
features = dataset.iloc[:, 1:].values
labels = dataset.iloc[:, :1].values
from sklearn.preprocessing import PolynomialFeatures
from sklearn.linear_model import LinearRegression
poly_object = PolynomialFeatures(degree = 5)
features_poly = poly_object.fit_transform(features)
lin_reg_2 = LinearRegression()
lin_reg_2.fit(features_poly, labels)
x=[[90,70,150]]
print(lin_reg_2.predict(poly_object.transform(x)))
#second
import statsmodels.api as sm
features = sm.add_constant(features)
features_opt = features[:, [0, 1, 2, 3]]
list1=[0,1,2,3]
features_opt = features[:, list1]
regressor_OLS = sm.OLS(endog = labels, exog = features_opt).fit()
while(len(regressor_OLS.pvalues)>1):
    regressor_OLS = sm.OLS(endog = labels, exog = features_opt).fit()
    index=regressor_OLS.pvalues.argmax()
    list1.pop(index)
    features_opt = features[:, list1]
    regressor_OLS = sm.OLS(endog = labels, exog = features_opt).fit()
    print(regressor_OLS.pvalues)
print ("Output : Brain Size is the only factor which is more useful in predicting intelligence.")

