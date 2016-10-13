#!/usr/bin/env python
# -*- coding: utf-8 -*-
from matplotlib.finance import quotes_historical_yahoo_ochl
import pandas as pd
import datetime
import numpy as np
__author__ = 'wangjj'
__mtime__ = '20161013下午 9:26'
today = datetime.date.today()
start = (today.year - 1, today.month, today.day)
quotes = quotes_historical_yahoo_ochl('AXP', start, today)
fields = ['date', 'open', 'close', 'high', 'low', 'volume']
ls = []
for i in range(0, len(quotes)):
    x = datetime.date.fromordinal(int(quotes[i][0]))
    y = datetime.datetime.strftime(x, '%Y-%m-%d')
    ls.append(y)
df = pd.DataFrame(quotes, index=ls, columns=fields)
df = df.drop(['date'], axis=1)
print df
print df.sort(columns='close',ascending=False)[0:5]
print df.sort_values(by='close',ascending=False)[:5]
print df.sort_values(by='close',ascending=False)[-5:]
print len(df[df.close > df.open])
status = np.sign(np.diff(df.close))
print status
ls_temp = []
for i in ls:
    ls_temp.append(datetime.datetime.strptime(i, '%Y-%m-%d').month)
ls_temp_set = set(ls_temp)
for i in ls_temp_set:
    print (i, ls_temp.count(i))
temp_df = df.copy()
temp_df['month'] = ls_temp
print temp_df['month'].value_counts()
print temp_df.groupby('month').count()
print temp_df.groupby('month').sum().volume
g = temp_df.groupby('month')
print g['volume'].sum()

