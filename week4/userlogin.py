#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = 'wangjj'
__mtime__ = '20161009下午 8:22'
__doc__ = '''
用字典创建一个平台的用户信息（包含用户名和密码）管理系统，
新用户可以用与现有系统帐号不冲突的用户名创建帐号，
已存在的老用户则可以用用户名和密码登陆重返系统。
'''
user = {
    'wangjj': '123456',
    'zhangff': '123456'
}


def new_user():
    global user
    name = raw_input('please enter your name :')
    while True:
        if user.get(name):
            name = raw_input('the user is existed,please enter your name again :')
        else:
            password = raw_input('please set your password :')
            user[name] = password
            print user


def old_user():
    # pass
    global user

    while True:
        name = raw_input('please enter your name :')
        password = raw_input('please enter your password :')
        if password == user.get(name):
            print name, 'welcome back'
            break
        else:
            print 'login incorrect'

    # print '123'


def login():
    option = """
                (N)ew User Login
                (O)ld User Login
                (E)xit
                """
    print option

    while True:
        try:
            choice = raw_input('Please enter your choice :')
            choice = choice.lower()
            if choice in ['n', 'o', 'e']:
                break
        except Exception as e:
            print e
            choice = raw_input('Please enter your choice :')
    if choice == 'n':
        new_user()
    elif choice == 'o':
        old_user()
    elif choice == 'e':
        print 'byebye'
        exit()


if __name__ == '__main__':
    login()
