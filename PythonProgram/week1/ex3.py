# -*- coding: utf-8
__author__ = 'wangjj'
__doc__ = '格式输出九九乘法表'
for i in range(1, 10):
    for j in range(1, i + 1):
        print "%d * %d = %2d " % (i, j, i * j),
    print ''
