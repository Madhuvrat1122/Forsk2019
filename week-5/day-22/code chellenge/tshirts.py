# -*- coding: utf-8 -*-
"""
Created on Tue Jun  4 11:23:54 2019

@author: mv gupta
"""
import numpy as np
from sklearn.cluster import DBSCAN
from sklearn import metrics
from sklearn.datasets.samples_generator import make_blobs
from sklearn.preprocessing import StandardScaler

dataset = pd.read_csv('tshirts.csv')
features = dataset.iloc[:, [1, 2]].values
plt.scatter(features[:,0], features[:,1])
plt.show()
centers = [[1, 1], [-1, -1], [1, -1]]
features, labels = make_blobs(n_samples=750, centers=centers, cluster_std=0.4,
                            random_state=0)

features = StandardScaler().fit_transform(features)

# #############################################################################
# Compute DBSCAN
db = DBSCAN(eps=0.3, min_samples=10).fit(features)
#core_samples_mask = np.zeros_like(db.labels_, dtype=bool)
#core_samples_mask[db.core_sample_indices_] = True
labels_pred = db.labels_
import matplotlib.pyplot as plt


plt.scatter(features[labels_pred == 0,0], features[labels_pred == 0,1],c='r', marker='+',label = 'Large')
plt.scatter(features[labels_pred == 1,0], features[labels_pred == 1,1],c='g', marker='o',label = 'Small' )
plt.scatter(features[labels_pred == 2,0], features[labels_pred == 2,1],c='b', marker='s',label = 'Medium' )
plt.scatter(features[labels_pred == -1,0],features[labels_pred == -1,1],c='y', marker='*' )