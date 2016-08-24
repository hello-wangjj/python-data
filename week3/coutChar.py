# -*-coding:utf-8
def countChar(s):
    count = [0] * 26
    for c in s:
        if c.isalpha():
            index = ord(c) - ord('a')
            count[index] += 1
    return count
a = raw_input('please input a string')
ls = countChar(a)
print ls
