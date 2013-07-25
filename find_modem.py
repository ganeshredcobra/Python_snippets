import os
import serial
import commands
import time

devs = []
ret = []

def iden_port():
	raw=commands.getoutput("dmesg | grep 'GSM modem (1-port) converter now attached to'")
	mod=raw.splitlines()
	mod_port=mod[-3:]
	for i in range(len(mod_port)):
		devs.append(mod_port[i][-7:])

def main():
	
	def sendCommand(com):
		ser.write(com+"\r\n")
		time.sleep(2)	
		while ser.inWaiting() > 0:
			msg = ser.readline().strip()
			msg = msg.replace("\r","")
			msg = msg.replace("\n","")
			if msg!="":
				ret.append(msg)
	print devs
	iden_port()
	print devs
	for i in range(len(devs)):
		print devs[i]
		ser=serial.Serial('/dev/%s'%devs[i], baudrate=115200, timeout=.1, rtscts=0)
		sendCommand("ATi")
		#print ret
		#print ret[0]
		if ret[0] == "Manufacturer: +GMI: HUAWEI TECHNOLOGIES CO., LTD":
			print ":)"
			break
		else:
			pass

if __name__ == "__main__":
	main()
