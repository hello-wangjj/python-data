#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = 'wangjj'
__mtime__ = '20161025下午 7:34'


class roster(object):
    """student and teacher class"""
    teacher = ''
    students = []

    def __init__(self, tn='Niuyun'):
        super(roster, self).__init__()
        self.teacher = tn

    def add(self, sn):
        self.students.append(sn)

    def remove(self, sn):
        self.students.remove(sn)

    def print_all(self):
        print 'Teacher:', self.teacher
        print 'Students:', self.students
if __name__ == '__main__':
    ros = roster()
    ros.add('wangjj')
    ros.print_all()