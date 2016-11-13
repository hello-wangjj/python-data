#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = 'wangjj'
__mtime__ = '20161113下午 3:34'
def main():
    file1 = open('TeleAddressBook.txt', 'r')
    file2 = open('EmailAddressBook.txt', 'r')
    # 跳过抬头
    file1.readline()
    file2.readline()
    lines1=file1.readlines()
    lines2=file2.readlines()
    list1_name=[]
    list2_name=[]
    list1_tele=[]
    list2_email=[]
    for line in lines1:
        elements=line.split()
        list1_name.append(str(elements[0]))
        list1_tele.append(str(elements[1]))
    for line in lines2:  # 获取第二个文本中的姓名和邮件信息
        elements = line.split()
        list2_name.append(str(elements[0]))
        list2_email.append(str(elements[1]))
    ###开始处理###
    lines = []
    lines.append('姓名\t    电话   \t  邮箱\n')
    # 按索引方式遍历姓名列表1
    for i in range(len(list1_name)):
        s = ''
        if list1_name[i] in list2_name:
            j = list2_name.index(list1_name[i])  # 找到姓名列表1对应列表2中的姓名索引位置
            s = '\t'.join([list1_name[i], list1_tele[i], list2_email[j]])
            s += '\n'
        else:
            s = '\t'.join([list1_name[i], list1_tele[i], str('   -----   ')])
            s += '\n'
        lines.append(s)

    # 处理姓名列表2中剩余的姓名
    for i in range(len(list2_name)):
        s = ''
        if list2_name[i] not in list1_name:
            s = '\t'.join([list2_name[i], str('   -----   '), list2_email[i]])
            s += '\n'
        lines.append(s)

    file3 = open('AddressBook.txt', 'w')
    file3.writelines(lines)
    file3.close()
    file1.close()
    file2.close()

    print("The addressBooks are merged!")

if __name__ == '__main__':
    main()