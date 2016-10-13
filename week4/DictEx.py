#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = 'wangjj'
__mtime__ = '20161011上午 10:50'
user = {
    'xiaoyun': '88888',
    'xiaohong': '5555555',
    'xiaoteng': '11111',
    'xiaoyi': '1234321',
    'xiaoyang': '1212121'
}


def look_for_user():
    name = raw_input("Please input the name:")
    global user
    while True:
        if user.get(name):
            print user.get(name)
            break
        else:
            print 'the name is not existed'
            name = raw_input("Please input the name again:")


def search_number():
    global user
    users = []
    for k, v in user.items():
        if len(v) > 5:
            users.append(k)
    print users


if __name__ == '__main__':
    option = """
                    (L)ook For User
                    (W)ho has the nice QQ number
                    (E)xit
                    """
    print option
    while True:
        try:
            choice = raw_input('Please enter your choice :')
            choice = choice.lower()
            if choice in ['l', 'w', 'e']:
                break
        except Exception as e:
            print e
            choice = raw_input('Please enter your choice :')
    if choice == 'l':
        look_for_user()
    elif choice == 'w':
        search_number()
    elif choice == 'e':
        print 'byebye'
        exit()
