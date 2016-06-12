#-*-coding:utf-8-*-

#找前5个默尼森数。P是素数且M也是素数，并且满足等式M=2**P-1，则称M为默尼森数。例如，P=5，M=2**P-1=31，5和31都是素数，因此31是默尼森数。
import math
def isPrime(x):
	# pass
	flag=True
	k=int(math.sqrt(x))
	for i in range(2,k+1):
		if x%i==0:
			flag=False
			return False
	if flag:
		return True


def isMonishen():
	for p in range(2,10000):
		for m in range(p,10000):
			if m-2**p==-1 and isPrime(p) and isPrime(p):
				print m,p

isMonishen()





