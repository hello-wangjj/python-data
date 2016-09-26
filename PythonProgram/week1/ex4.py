# -*- coding: utf-8
__author__ = 'wangjj'
__doc__ = '猴子吃桃问题，每次循环右移一位'
n = 1
for i in range(5, 0, -1):
    n = (n + 1) << 1
print n
