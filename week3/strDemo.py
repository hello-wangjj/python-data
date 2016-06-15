#-*-coding:utf-8-*-
# 使用以下语句存储一个字符串：
#   str = 'My moral standing  is: 0.98765'
# 将其中的数字字符串转换成浮点数并输出。  
# （提示：可以使用find方法和字符串切片，提取出字符串中冒号后面的部分，然后使用float函数，将提取出来的字符串转换为浮点数）

s = 'My moral standing  is: 0.98765'
num=float(s.split(' ')[-1])
print num

#2. 输入一个字符串“I like Python very much 2333 because Python is very cute 666.”，判别该字符串中数字字符和单词的个数，并将第一次出现的Python替换成你偶像的名字并输出新字符串。
s2='I like Python very much 2333 because Python is very cute 666.'

count_numer=0
count_word=0
ls=s2.split('.')[0].split(' ')
print ls
for i in ls:
	if i.isdigit():
		count_numer+=1
	if i.isalpha():
		count_word+=1
print count_numer,count_word
s3=s2.replace('Python', 'wangjj',1)
print s3
