#!/usr/bin/env python
# -*- coding: utf-8 -*-
from matplotlib.finance import quotes_historical_yahoo_ochl
from datetime import date, datetime
import pandas as pd
__author__ = 'wangjj'
__mtime__ = '20161011下午 4:52'
today = date.today()
start = (today.year - 1, today.month, today.day)
quotes = quotes_historical_yahoo_ochl('AXP', start, today)
fields = ['date', 'open', 'close', 'high', 'low', 'volume']
ls = []
for i in range(0, len(quotes)):
    x = date.fromordinal(int(quotes[i][0]))
    y = datetime.strftime(x, '%Y-%m-%d')
    ls.append(y)

df = pd.DataFrame(quotes, index=ls, columns=fields)
df = df.drop(['date'], axis=1)
print today, start
print type(quotes)
print df
