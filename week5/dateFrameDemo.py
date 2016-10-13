#!/usr/bin/env python
# -*- coding: utf-8 -*-
import pandas as pd
__author__ = 'wangjj'
__mtime__ = '20161012下午 7:15'
dates = pd.date_range(start='20150201', periods=10)
lsA = ['value']
result = pd.DataFrame(range(1, 11), index=dates, columns=lsA)
print result
print '-------'
dates = pd.date_range(start='20150201', periods=5)
data = {
    'A': [1, 3, 5, 7, 9],
    'B': [2, 4, 6, 8, 10]
}
res = pd.DataFrame(data=data, index=dates)
print res
print '-------'
print res.loc[u'2015-02-02':u'2015-02-04', ['B']]
print res.loc[u'2015-02-02':u'2015-02-04', 'B']
print res.iloc[1:4, [1]]
print '-------'
print res.loc['2015-02-02':'2015-02-05', ['A', 'B']]
print '-------'
print res.ix['2015-02-03', 'B']
print res.loc['2015-02-03', 'B']
print '-------'
print res.iloc[1:4, [0]]
print '-------'
print res.iloc[1, 1]
print res.iat[1, 1]
print '-------'
print res[(res.index>'2015-02-03')&(res.A>8)]