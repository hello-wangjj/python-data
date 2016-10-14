#!/usr/bin/env python
# -*- coding: utf-8 -*-
import turtle
__author__ = 'wangjj'
__mtime__ = '20161014上午 11:16'


def draw_snake(rad, angle, length, neckrad):
    for i in range(length):
        turtle.circle(rad, angle)
        if i / 2 == 0:
            turtle.pencolor('red')
        else:
            turtle.pencolor('blue')
        turtle.circle(-rad, angle)
    turtle.circle(rad, angle / 2)
    turtle.fd(rad)
    turtle.circle(neckrad + 1, 180)
    turtle.fd(rad * 2 / 3)


def main():
    turtle.setup(1300, 800, 10, 10)
    pensize = 30
    turtle.pensize(pensize)
    turtle.pencolor('blue')
    turtle.seth(-40)
    draw_snake(40, 80, 5, pensize / 2)
    turtle.done()
if __name__ == '__main__':
    # print help(turtle)
    main()
