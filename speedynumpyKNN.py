# -*- coding: utf-8 -*-
"""
Created on Mon Oct 12 11:06:21 2015

@author: Jordan Poles

Inspiration from https://speakerdeck.com/pycon2015/jake-vanderplas-losing-your-loops-fast-numerical-computing-with-numpy
"""
#Libs
import numpy as np
from sklearn.neighbors import NearestNeighbors
#Generate Data to cluster
data = np.random.random((1000,3)) #1000 pts in 3D
#Get diffs by coord
diff = data.reshape(1000, 1, 3) - data
#Square and sum differences to get distances
dists = (diff ** 2).sum(2)
#Set diagonal equal to infiity (self matches cannot be nn)
i = np.arange(1000)
dists[i, i] = np.inf
#Find minimum value for each pt
nn = np.argmin(dists, 1);
#Validation
sknn = NearestNeighbors().fit(data).kneighbors(data,2)[1][:,1]
sknn == nn