import cv2
import serial
import numpy as np
ser = serial.Serial(port='/dev/ttyUSB0',baudrate=9600)
print ser.portstr
cam=cv2.VideoCapture(0)
f=0
b=0
s=0
l=0
r=0
while True:
	returnVal,frame=cam.read()
	img=cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
	red_lower=np.array([0,150,150],np.uint8)
	red_upper=np.array([10,255,255],np.uint8)
	red=cv2.inRange(img,red_lower,red_upper)
	M = cv2.moments(red)
	if M['m00']==0:
		x = 0
		y = 0
	else:
		x = int(M['m10']/M['m00'])
		y = int(M['m01']/M['m00'])
	
	if 10<x<280:
		if 170<y<330:
			if f==0:
				ser.write("F")
				f=1
				l=0
				r=0
				b=0
				s=0
		elif 10<y<170:
			if l==0:
				ser.write("R")
				l=1
				f=0
				r=0
				b=0
				s=0

		elif 330<y<490:
			if r==0:
				ser.write("L")
				r=1
				l=0
				f=0
				b=0
				s=0

	elif 370<x<640:
		if 170<y<330:
			if b==0:
				ser.write("B")
				b=1
				l=0
				r=0
				f=0
				s=0

		elif 10<y<170:
			if r==0:
				ser.write("r")
				r=1
				l=0
				f=0
				b=0
				s=0

		elif 330<y<490:
			if l==0:
				ser.write("l")
				l=1
				f=0
				r=0
				b=0
				s=0
	else:
		if s==0:
			ser.write("S")
			s=1
			l=0
			r=0
			b=0
			f=0
	cv2.imshow('gold fish', red)
	print x, y
	key=cv2.waitKey(1) % 0x100
	if key == 27:
		ser.close()
		break

