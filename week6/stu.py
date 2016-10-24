#!/usr/bin/env python
# -*- coding: utf-8 -*-
import pandas as pd
__author__ = 'wangjj'
__mtime__ = '20161023上午 11:39'
stu = pd.read_excel('stu.xlsx')
print stu
print stu['math'], len(stu['math'])
print stu.loc[1]['math']
print len(stu.index)
list_temp = []
for i in range(len(stu.index)):
    list_temp.append(stu.loc[i]['python'] + stu.loc[i]['math'])
stu['Sum_score'] = list_temp
print stu
stu.to_excel('stu.xlsx', sheet_name='score')