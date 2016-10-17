#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = 'wangjj'
__mtime__ = '20161015下午 4:10'
print '{} {} {}'.format("wangjj", 'is', 'a good boy')
print '{0} {1} {2}'.format("wangjj", 'is', 'a good boy')
print '{1} {2} {0}'.format("wangjj", 'is', 'a good boy')
s = '圆周率{{{1}{2}{0}}}'
print s
print s.format('是', '3.1415926', '...')
print '{0:-^10} {1} {2}'.format("wangjj", 'is', 'a good boy')
print len('老师好')
a = "abcd1234"
print a.replace('c', 'C')
print a.find('cd')
print len(str(pow(2, 1000)))
for i in range(5):
    print ('*'*i)
