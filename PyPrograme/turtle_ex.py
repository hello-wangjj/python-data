#!/usr/bin/env python
# -*- coding: utf-8 -*-
import turtle
__author__ = 'wangjj'
__mtime__ = '20161024下午 11:35'


def make_line(pen):
    pen.forward(30)


def main():
    p = turtle.Turtle()
    p.color('black')
    p.pensize(5)
    p.speed(10)
    p.hideturtle()
    p.penup()
    p.goto(-100, 50)
    p.pendown()
    make_line(p)
    p.right(90)
    make_line(p)
    p.right(90)
    make_line(p)
    p.left(90)
    make_line(p)
    p.left(90)
    make_line(p)
    turtle.done()


if __name__ == '__main__':
    main()
