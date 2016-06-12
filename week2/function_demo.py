#-*-coding:utf-8-*-
def addMe2Me(x):
	'apply operation + to argument'
	return (x+x)

#按公式：C= 5/9×(F-32) ，将华氏温度转换成摄氏温度，并产生一张华氏0～300度与对应的摄氏温度之间的对照表（每隔20度输出一次）
#验证命题：如果一个三位整数是37的倍数，则这个整数循环左移后得到的另两个3位数也是37的倍数。
#（注意验证命题的结果输出方式，只要输出命题为真还是假即可，而非每一个三位数都有一个真假的输出）



def H2C(F):
	return 5.0/9*(F-32)


def is37(x):
	if x%37==0:
		temp=x/10
		last=x%10
		newX=last*100+temp
		if newX%37==0:
			print True
		else:
			print False

if __name__=='__main__':
	print addMe2Me.__doc__
	c=addMe2Me(3)
	print c
	for i in range(0,301,20):
		# print H2C(i),
		print	'%06.2f'%H2C(i),
		if i%100==0:
			print 

	for i in range(100,1000):
		is37(i)


