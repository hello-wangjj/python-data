#!/usr/bin/env python
# -*- coding: utf-8 -*-
from pylab import *
from scipy.cluster.vq import *
__author__ = 'wangjj'
__mtime__ = '20161022下午 5:10'
ls1 = [88.0, 64.0, 96.0, 85.0]
ls2 = [92.0, 99.0, 95.0, 94.0]
ls3 = [91.0, 87.0, 95.0, 94.0]
ls4 = [78.0, 99.0, 97.0, 81.0]
ls5 = [88.0, 78.0, 98.0, 84.0]
ls6 = [100.0, 95.0, 100.0, 92.0]
data = vstack((ls1, ls2, ls3, ls4, ls5, ls6))
centroids, _ = kmeans(data, 2)
result, _ = vq(data, centroids)
print result
