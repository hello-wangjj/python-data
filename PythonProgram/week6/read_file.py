#!/usr/bin/env python
# -*- coding: utf-8 -*-
import turtle
__author__ = 'wangjj'
__mtime__ = '20161113下午 3:00'


def main():

    turtle.title('数据驱动的路径绘制')
    turtle.setup(800, 600, 0, 0)
    p = turtle.Turtle()
    p.color('red')
    p.width(5)
    p.shape('turtle')
    p.speed(5)
    result = []
    file = open('data.txt', 'r')
    for line in file:
        result.append(list(map(float, line.split(','))))
    print result
    for i in range(len(result)):
        p.color((result[i][3], result[i][4], result[i][5]))
        p.forward(result[i][0])
        if result[i][1]:
            p.right(result[i][2])
        else:
            p.left(result[i][2])
    p.goto(0, 0)
if __name__ == '__main__':
    main()
