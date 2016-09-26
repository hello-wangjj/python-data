# -*- coding: utf-8
__author__ = 'wangjj'


def count_char(string):
    ls = [0] * 26
    string = string.lower()
    for ch in string:
        if ch.isalpha():
            index = ord(ch) - ord('a')
            ls[index] += 1
    return ls
if __name__ == "__main__":
    string = raw_input()
    print count_char(string)
