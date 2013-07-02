import os
os.system('touch /tmp/dev.txt')
os.system('sudo wvdialconf > /tmp/dev.txt')
file=open('/tmp/dev.txt','r+')
re=file.read()
f=re.splitlines()
b=f[5]
po=b[-8:-1]
if po[:6]=="ttyUSB":
	print po
else:
	print "error"
