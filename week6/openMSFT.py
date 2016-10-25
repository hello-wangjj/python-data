#!/usr/bin/env python
# -*- coding: utf-8 -*-
import time
from matplotlib.finance import quotes_historical_yahoo_ochl
from datetime import date
from datetime import datetime
import pandas as pd
import matplotlib.pyplot as plt
import ch
ch.set_ch()
__author__ = 'wangjj'
__mtime__ = '20161023下午 10:11'
start = datetime(2015, 1, 1)
end = datetime(2015, 12, 31)
quotes = quotes_historical_yahoo_ochl('MSFT', start, end)
fields = ['date', 'open', 'close', 'high', 'low', 'volume']
list1 = []
list2 = []
for i in range(0, len(quotes)):
    x = date.fromordinal(int(quotes[i][0]))
    y = datetime.strftime(x, '%y/%m/%d')
    list1.append(y)
    list2.append(x.month)
# print(list1)
quotes_of_MSFT = pd.DataFrame(quotes, index=list1, columns=fields)
quotes_of_MSFT = quotes_of_MSFT.drop(['date'], axis=1)
quotes_of_MSFT['month'] = list2
# print(quotes_of_MSFT)
open_MSFT = quotes_of_MSFT.groupby('month').mean().open
print open_MSFT, open_MSFT.index
list_open = []
for i in range(1, 13):
    list_open.append(open_MSFT[i])
plt.subplot(121)
plt.plot(open_MSFT.index, list_open, 'r-.*')
plt.subplot(122)
plt.plot(open_MSFT.index, open_MSFT.values)
plt.show()
print type(open_MSFT)
open_MSFT.plot()
plt.show()
# inter
quotesINT = quotes_historical_yahoo_ochl('INTC', start, end)
quotes_of_INT = pd.DataFrame(quotesINT, columns=fields)
list3 = []
for i in range(0, len(quotesINT)):
    x = date.fromordinal(int(quotesINT[i][0]))
    y = date.strftime(x, '%y/%m/%d')
    list3.append(y)
quotes_of_INT.index = list3
quotes_of_INT = quotes_of_INT.drop(['date'], axis=1)
quotes_of_INT15 = quotes_of_INT['15/01/01':'15/12/31']
print 'inter'
quotes_of_INT15.open.plot()
plt.show()

# compare
compare_ms_in = pd.DataFrame()
compare_ms_in['ms'] = quotes_of_MSFT.open
compare_ms_in['in'] = quotes_of_INT.open
compare_ms_in.plot(title=u'微软和英特尔的开盘价')
plt.show()
plt.scatter(quotes_of_MSFT.close - quotes_of_MSFT.open, quotes_of_MSFT.volume)
plt.show()
