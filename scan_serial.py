#! /usr/bin/env python

import os,sys,serial,commands
currentUser = commands.getoutput("whoami")

def scan():
    """scan for available ports. return a list of tuples (num, name)"""
    available = []
    for i in range(256):
        try:
            s = serial.Serial(i)
            available.append( (i, s.portstr))
            s.close()  
        except serial.SerialException:
            pass
    return available

if __name__=='__main__':
    if currentUser != 'root':
        print "You need to be root!"
        sys.exit()
    else:
        print "Found ports:"
        for n,s in scan():
            print "(%d) %s" % (n,s)
            ser = serial.Serial('%s'%s, 115200, timeout=1)
            while True:
                data=ser.read()
                if data!='':
                    file=open('/var/www/serial.txt','w')                   
                    #print "created file"
                elif data=='':
                    if os.path.isfile('/var/www/serial.txt')==True:
                        os.chdir('/var/www')
                        os.remove('serial.txt')
                        #print "removed file"

                
            
