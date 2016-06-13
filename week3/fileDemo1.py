f=open('FirstFile.txt','r+')
f.seek(0,2)
f.write('wangjj world!')
f.close()
f=open('FirstFile.txt','r')
p1=f.read()
p2=f.read()
print p1,p2
f.close()
