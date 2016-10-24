#!/usr/bin/env python
# -*- coding: utf-8 -*-
import pandas as pd
__author__ = 'wangjj'
__mtime__ = '20161023上午 12:21'
data = {
    'Singer': ['The rolling stones', 'Beatles', "Guns N'Roses", 'Metallica'],
    'Song': ['Satisfaction', 'Let It Be', "Don't Cry", 'Nothing Else Matters']
}
singer = pd.DataFrame(data=data)
print singer
singer.to_csv('singer.csv')
singer2 = pd.read_csv('singer.csv')
print singer2
