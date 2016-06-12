import math

for i in range(2,101):
	flag=True
	k=int(math.sqrt(i))
	for j in range(2,k+1):
		if i%j==0:
			flag=False
			break
	if flag:
		print i,
			