#!/usr/bin/env python
# -*- coding: utf-8 -*-
import urllib
# import re

url1 = 'http://tieba.baidu.com/p/100000000'
text1 = '100000000'
for i in range(10):
    url2 = url1 + str(i)
    r = urllib.urlopen(url2)
    html = r.read()
    textName = text1 + str(i)+'.html'
    fileName = open(textName, 'wb')
    fileName.write(html)
