import serial
import subprocess
import time

ser = serial.Serial(
    port='/dev/ttyACM0',\
    baudrate=9600,\
        timeout=0)

print("connected to: " + ser.portstr)
thirsty = 'Give me Water Feeling Thirsty '
happy = 'Got Water Happy '
#this will store the line
line = []
lastmsg = ""
while True:
    ser.flushInput()
    for c in ser.read():
        if c=='2':
	    msg = thirsty
	    print msg
	    if msg == lastmsg:
	    	print "Duplicate"
		time.sleep(5)
	    else:
		#command='twitter -e binuabraham990@email.com set %s' % msg
	    	command = 'fbcmd post "%s"'%msg
	    	lastmsg = msg
	    	subprocess.call(command, shell=True)
	elif c=='1':
	    msg = happy
	    print msg
	    if msg == lastmsg:
	    	print "Duplicate"
		time.sleep(5)
	    else:
		#command='twitter -e binuabraham990@email.com set %s' % msg
	    	command = 'fbcmd post "%s"'%msg
            	lastmsg = msg
	    	subprocess.call(command, shell=True)
            #print(''.join(line))
        break

ser.close()
