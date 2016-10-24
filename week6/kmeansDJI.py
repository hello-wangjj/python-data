#!/usr/bin/env python
# -*- coding: utf-8 -*-
from pylab import *
from scipy.cluster.vq import kmeans, vq
from matplotlib.finance import quotes_historical_yahoo_ochl
from datetime import datetime
__author__ = 'wangjj'
__mtime__ = '20161022下午 7:46'
start = datetime(2016, 7, 1)
end = datetime(2016, 9, 30)
listDji = [
    'AXP',
    'BA',
    'CAT',
    'CSCO',
    'CVX',
    'DD',
    'DIS',
    'GE',
    'GS',
    'HD',
    'IBM',
    'INTC',
    'JNJ',
    'JPM',
    'KO',
    'MCD',
    'MMM',
    'MRK',
    'MSFT',
    'NKE',
    'PFE',
    'PG',
    'T',
    'TRV',
    'UNH',
    'UTX',
    'V',
    'VZ',
    'WMT',
    'XOM']
quotes = [[0 for col in range(90)] for row in range(30)]
listTemp = [[0 for col in range(90)] for row in range(30)]
for i in range(30):
    quotes[i] = quotes_historical_yahoo_ochl(listDji[i], start, end)
    days = len(quotes[0])
for i in range(30):
    for j in range(days - 1):
        if (quotes[i][j][2] and quotes[i][j + 1][2]
                and (quotes[i][j + 1][2] >= quotes[i][j][2])):
            listTemp[i][j] = 1.0
        else:
            listTemp[i][j] = -1.0
data = vstack(listTemp)
centroids, _ = kmeans(data, 4)  # float or double is supported
result, _ = vq(data, centroids)
print(result)
