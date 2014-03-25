import cv2
import serial
import numpy as np
ser = serial.Serial(port='/dev/ttyUSB0',baudrate=9600)
print ser.portstr
cam=cv2.VideoCapture(0)
n=0
while True:
	returnVal,frame=cam.read()
	img=cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
	black_lower=np.array([0,0,0],np.uint8)
	black_upper=np.array([255,255,10],np.uint8)
	black=cv2.inRange(img,black_lower,black_upper)
	M = cv2.moments(black)
	if M['m00']==0:
		centroid_x = 0
		centroid_y = 0
	else:
		centroid_x = int(M['m10']/M['m00'])
		centroid_y = int(M['m01']/M['m00'])
	cv2.imshow('black molly', frame)
	print centroid_x, centroid_y
	n=n+1
	key=cv2.waitKey(1) % 0x100
	if key == 27:
		ser.close()
		break

