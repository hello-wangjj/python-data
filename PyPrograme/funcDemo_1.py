#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = 'wangjj'
__mtime__ = '20161023下午 11:42'


def add(amount, rate):
    for i in range(len(amount)):
        amount[i] = amount[i] * (1 + rate)


def main():
    amount = [100, 200, 300, 400]
    rate = 0.05
    add(amount, rate)
    print amount


if __name__ == '__main__':
    main()
