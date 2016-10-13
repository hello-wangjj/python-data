#!/usr/bin/env python
# -*- coding: utf-8 -*-
from pandas import Series, DataFrame

__author__ = 'wangjj'
__mtime__ = '20161010下午 11:04'
data = {'Scala': 2003, 'Java': 1995, 'Python': 1991, 'Go': 2009}
ser = Series(data)
print ser
print 'C' in ser
print 'Go' in ser
print ser.values.mean()
print '----'
datas = {
    'name': [
        'Wangdachui',
        'Linling',
        'Niuyun'],
    'pay': [
        4000,
        5000,
        6000]}
dataFra=DataFrame(datas)
print DataFrame(datas)
print '----'
print dataFra['name']
print '----'
print dataFra.pay
print '----'
print dataFra.head(2)
print '----'
print dataFra.tail(2)