import os

port="ttyUSB99"

PATH="docomo"
f=open('%s'%PATH)
line=f.readlines()
s=line[7]
n=s.split()
#val=raw_input("Enter Download Limit in MB: ")
#n[1]=val
#new=" ".join(n)
#print(new)
f.close()
fi=open('%s'%PATH)
files=fi.read()
#print(files)
text=files.replace('%s'%s,'%s \n'%port)
#print(text)
fil=open('%s'%PATH,'w+')
fil.write('%s'%text)
