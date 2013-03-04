import serial
from time import sleep
import os

port = "/dev/ttyUSB0"
ser = serial.Serial(port, 9600, timeout=0)
last_received = ''

buffer = ''

while True:
	# last_received = ser.readline()
	buffer += ser.read(ser.inWaiting())
	if '#' in buffer:
		last_received, buffer = buffer.split('#')[-2:]
		print last_received
		os.system("espeak '%s'"%last_received)
		#os.system("echo \'(voice_en1_mbrola)(SayText \'%s\')\' | festival",%a)
