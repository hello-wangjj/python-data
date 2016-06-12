def f(X):
	global a
	print a
	a=5
	print a+X

a=3
f(8)
print a