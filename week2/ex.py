def test(x):
	if isinstance(x, list):
		x.append(4)
		print x
	elif isinstance(x, int):
		x+=1
		print x


def test1(f,a,b):
	print(f(a,b))

def proc(n ):
    if (n<0):
        print '-', 
        n = -n
    if (n / 10):
        proc(n / 10 )
    print n % 10,

if __name__=='__main__':
	x=3
	test(x)
	test1((lambda x, y:x**3+y),2,3)
	print True==1
	a='1'
	b=2
	print a<b
	proc(-345)