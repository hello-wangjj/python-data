# -*- coding: utf-8
__author__ = 'wangjj'
n = raw_input('请输入一个整数 N ：')
while True:
    try:
        n = int(n)
        break
    except Exception as e:
        print e
        n = raw_input('请输入一个整数 N ：')
sum = 0
for i in range(n):
    sum += i + 1
print '1 到 N 求和结果: %d' % sum
