# -*- coding: utf-8
import math
__author__ = 'wangjj'


def prime(num):
    if num == 1:
        return False
    k = int(math.sqrt(num))
    for i in range(2, k + 1):
        if num % i == 0:
            return False
    return True


def monisen(no):
    start = 2
    count = 1
    while True:
        if prime(2**start-1):
            if count == no:
                return 2**start-1
            count += 1
        start += 1


print monisen(input())
