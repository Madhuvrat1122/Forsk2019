# -*- coding: utf-8 -*-
"""
Created on Tue Jun  4 09:09:13 2019

@author: mv gupta
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
dataset = pd.read_csv('deliveryfleet.csv')
features = dataset.iloc[:, [1, 2]].values
plt.scatter(features[:,0], features[:,1])
plt.show()
from sklearn.cluster import KMeans
#first solution
kmeans = KMeans(n_clusters = 2, init = 'k-means++', random_state = 0)
pred_cluster = kmeans.fit_predict(features)
plt.scatter(features[pred_cluster == 0, 0], features[pred_cluster == 0, 1], c = 'blue', label = 'Urban')
plt.scatter(features[pred_cluster == 1, 0], features[pred_cluster == 1, 1], c = 'red', label = 'Rural')
plt.scatter(kmeans.cluster_centers_[:, 0], kmeans.cluster_centers_[:, 1], c = 'yellow', label = 'Centroids')
plt.title('Clusters of datapoints')
plt.xlabel('Distance_Feature')
plt.ylabel('speeding_Feature')
plt.legend()
plt.show()
#second solution
kmeans = KMeans(n_clusters = 4, init = 'k-means++', random_state = 0)
pred_cluster = kmeans.fit_predict(features)
plt.scatter(features[pred_cluster == 0, 0], features[pred_cluster == 0, 1], c = 'blue', label = 'Urban_followed_speed')
plt.scatter(features[pred_cluster == 1, 0], features[pred_cluster == 1, 1], c = 'red', label = 'Rural_followed_speed')
plt.scatter(kmeans.cluster_centers_[:, 0], kmeans.cluster_centers_[:, 1], c = 'yellow', label = 'Centroids')
plt.title('Clusters of datapoints')
plt.xlabel('Distance_Feature')
plt.ylabel('speeding_Feature')
plt.legend()
plt.show()
#third solution
kmeans = KMeans(n_clusters = 4, init = 'k-means++', random_state = 0)
pred_cluster = kmeans.fit_predict(features)
plt.scatter(features[pred_cluster == 0, 0], features[pred_cluster == 0, 1], c = 'blue', label = 'Urban_followed_speed')
plt.scatter(features[pred_cluster == 1, 0], features[pred_cluster == 1, 1], c = 'red', label = 'Rural_followed_speed')
plt.scatter(features[pred_cluster == 2, 0], features[pred_cluster == 2, 1], c = 'green', label = 'Rural_over_speed')
plt.scatter(features[pred_cluster == 3, 0], features[pred_cluster == 3, 1], c = 'black', label = 'Urban_over_speed')
plt.scatter(kmeans.cluster_centers_[:, 0], kmeans.cluster_centers_[:, 1], c = 'yellow', label = 'Centroids')
plt.title('Clusters of datapoints')
plt.xlabel('Distance_Feature')
plt.ylabel('speeding_Feature')
plt.legend()
plt.show()

