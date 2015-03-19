#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  canmate_multi.py
#  
#  Copyright 2014 Deep Thought Systems <info@dthoughts.com>
#  
#  This program is free software; you can redistribute it and/or modify
#  it. For any support please contact in the above email.
#
#  Deep Thought Systems (P) Ltd
#  K-130, Kochar Road, Sasthamangalam
#  Thiruvananthapuram, Kerala - 695010, India
#  Contact No.: +91 471 406 6468
#  www.dthoughts.com
#
#  This Python program is for CANMate Hardware and supports both GNU/Linux and Windows.
#

import sys, serial
import numpy as np
from time import sleep
from collections import deque
from matplotlib import pyplot as plt
import platform
import time
import sys
import ctypes
import random
from ctypes import *

RPM=0
PLATFORM = platform.system()
if PLATFORM == "Windows":
    from ctypes.wintypes import *

    libCAN = ctypes.WinDLL("C:\WINDOWS\system32\CANMateDll.dll")
    libc = cdll.msvcrt
    printf = libc.printf
else:
    libCAN = cdll.LoadLibrary("libCANMATE.so")
    libc = CDLL("libc.so.6")
    printf = libc.printf

# Define the CAN Message struct
class CANMsg(Structure):
    _pack_ = 1
    _fields_ = [('bExtended', ctypes.c_ubyte),
                ('chTmStmpH', ctypes.c_ubyte),
                ('chTmStmpL', ctypes.c_ubyte),
                ('EArbId1', ctypes.c_ubyte),
                ('EArbId0', ctypes.c_ubyte),
                ('SArbId1', ctypes.c_ubyte),
                ('SArbId0', ctypes.c_ubyte),
                ('DLC', ctypes.c_ubyte),
                ('D0', ctypes.c_ubyte),
                ('D1', ctypes.c_ubyte),
                ('D2', ctypes.c_ubyte),
                ('D3', ctypes.c_ubyte),
                ('D4', ctypes.c_ubyte),
                ('D5', ctypes.c_ubyte),
                ('D6', ctypes.c_ubyte),
                ('D7', ctypes.c_ubyte)]


def from_param(self):
    return ctypes.c_void_p(self.c_ptr)


# Define the CAN Event struct
class CANEvent(Structure):
    _fields_ = [('chErr', ctypes.c_ubyte),
                ('chTxErrCnt', ctypes.c_ubyte),
                ('chRxErrCnt', ctypes.c_ubyte)]

class AnalogData:
  # constr
  def __init__(self, maxLen):
    self.ax = deque([0.0]*maxLen)
    self.ay = deque([0.0]*maxLen)
    self.maxLen = maxLen

  # ring buffer
  def addToBuf(self, buf, val):
    if len(buf) < self.maxLen:
      buf.append(val)
    else:
      buf.pop()
      buf.appendleft(val)

  # add data
  def add(self, data):
    #assert(len(data) == 2)
    self.addToBuf(self.ax, data)
    self.addToBuf(self.ay, data)
    
# plot class
class AnalogPlot:
  # constr
  def __init__(self, analogData):
    # set plot to animated
    plt.ion() 
    self.axline, = plt.plot(analogData.ax)
    self.ayline, = plt.plot(analogData.ay)
    plt.ylim([0, 2000])

  # update plot
  def update(self, analogData):
    self.axline.set_ydata(analogData.ax)
    self.ayline.set_ydata(analogData.ay)
    plt.draw()

#Datacallback function
def Datacalbk(a, b):
    #print "Received: "
    #printf("Recv Value: %02X %02X %02X %02X %02X %02X %02X %02X %02X %02X %02X %02X %02X %02X %02X %02X\n",
           #a[0].bExtended, a[0].chTmStmpH, a[0].chTmStmpL, a[0].EArbId1, a[0].EArbId0, a[0].SArbId1, a[0].SArbId0,
           #a[0].DLC, a[0].D0, a[0].D1, a[0].D2, a[0].D3, a[0].D4, a[0].D5, a[0].D6, a[0].D7)
    printf("Recv Value: %02X %02X %02X %02X %02X %02X %02X %02X %02X\n",a[0].DLC, a[0].D0, a[0].D1, a[0].D2, a[0].D3, a[0].D4, a[0].D5, a[0].D6,
	 a[0].D7)
    A=a[0].D3
    B=a[0].D4
    if(a[0].D2 == 0x0C):
    	rpm=((A*256)+B)/4
    	print rpm
    	analogData.add(rpm)
    #else:
#	speed=a[0].D2
#	analogData.add(speed)

    #analogPlot.update(analogData)
    return 0

#Eventcallback function
def Eventcalbk(a):
    print "Event Occured\n"
    print a[0].chErr, a[0].chTxErrCnt, a[0].chRxErrCnt
    return 0


def Help():
    print "Possible Option are :"
    print "open, version, setbaud, getbaud, loop/normal, recep, write, exit\n"


#Variables
ret_check = c_int(0)
handle = c_void_p()
num = c_int(1)

#Index no for Baudrate
"""
 BAUD_RATE33K	1
 BAUD_RATE50K	2
 BAUD_RATE80K	3
 BAUD_RATE83K	4
 BAUD_RATE100K	5
 BAUD_RATE125K	6
 BAUD_RATE200K	7
 BAUD_RATE250K	8
 BAUD_RATE500K	9
 BAUD_RATE625K	10
 BAUD_RATE800K	11
 BAUD_RATE1000K	12
"""
chBaudRate = c_int(9) #BAUD_RATE500K	9

#pmsg = CANMsg(0, 0, 0, 0, 0, 0, 8, 8, 0x41, 0x0C, 0x0D, 0xCA, 0, 0, 0, 0) #  initially memset to {0}
#pmsg = CANMsg(0, 0, 0, 0, 0, 0x07, 0xE0, 8, 0x02, 0x01,0x0C, 0, 0, 0, 0, 0) #  initially memset to {0}
pmsg = CANMsg(0, 0, 0, 0, 0, 7, 0xE0, 8, 2, 1, 0x0C, 0, 0, 0, 0, 0) 

libCAN.WriteCANMessage.argtypes = [handle, POINTER(CANMsg)]

#Datacallback and Eventcallback function declaration
DataCB = CFUNCTYPE(c_int, POINTER(CANMsg), POINTER(c_int))
EventCB = CFUNCTYPE(c_int, POINTER(CANEvent))
_data_fn = DataCB(Datacalbk)
_event_fn = EventCB(Eventcalbk)

libCAN.OpenCANMate.argtypes = [DataCB, EventCB]

#GetBaudRate function declaration
GetBRate = libCAN.GetCurrentBaudRate
GetBRate.restype = c_int
GetBRate.argtypes = [handle, POINTER(c_int)]
Data = c_int()

#GetFirmware Version
GetVer = libCAN.GetFirmwareVersion
GetVer.restype = c_int
GetVer.argtypes = [handle, POINTER(c_int)]
Ver = c_int()

Help()
#input = raw_input("Enter the command : ")
#if input == "open":
handle = libCAN.OpenCANMate(_data_fn, _event_fn)
    #print handle
if (handle > 0):
	print "Open Sucess"
else:
	print "Error Opening"
ret_check = libCAN.SetCANBaudRate(handle, chBaudRate)
if (ret_check == 0):
    print "CAN Baudrate of 500K Configured"
else:
    print "CAN Baudrate Config failed"
        #print ret_check
ret_check = libCAN.SetNormalMode(handle)
if (ret_check == 0):
	print "Normal Mode Configured"
else:
	print "Normal Mode  failed"

#ret_check = libCAN.SetLoopbackMode(handle)
#if (ret_check == 0):
#	print "Loop Back Mode Configured"
#else:
#	print "Loop Back Mode  failed"
        #print ret_check
#elif input == "recep":
ret_check = libCAN.StartReception(handle)
if (ret_check == 0):
	print "Reception Started"
else:
	print "Reception failed"
analogData = AnalogData(100)
analogPlot = AnalogPlot(analogData)
while True:
	#pmsg.D1=0x0C
	#pmsg.D2=random.randrange(0x0,0x0F)
	#pmsg.D3=random.randrange(0x0,0x0F)
	printf("Send Value: %02X %02X %02X %02X %02X %02X %02X %02X %02X %02X %02X %02X %02X %02X %02X %02X\n",
			   pmsg.bExtended, pmsg.chTmStmpH, pmsg.chTmStmpL, pmsg.EArbId1, pmsg.EArbId0, pmsg.SArbId1, pmsg.SArbId0,
			   pmsg.DLC, pmsg.D0, pmsg.D1, pmsg.D2, pmsg.D3, pmsg.D4, pmsg.D5, pmsg.D6, pmsg.D7)
	ret_check = libCAN.WriteCANMessage(handle, byref(pmsg))
	time.sleep(0.5)
	#pmsg.D1=0x0D
	#pmsg.D2=random.randrange(0x0,0x0F)
	#pmsg.D3=random.randrange(0x0,0x0F)
	#printf("Send Value: %02X %02X %02X %02X %02X %02X %02X %02X %02X %02X %02X %02X %02X %02X %02X %02X\n",
	#		   pmsg.bExtended, pmsg.chTmStmpH, pmsg.chTmStmpL, pmsg.EArbId1, pmsg.EArbId0, pmsg.SArbId1, pmsg.SArbId0,
	#		   pmsg.DLC, pmsg.D0, pmsg.D1, pmsg.D2, pmsg.D3, pmsg.D4, pmsg.D5, pmsg.D6, pmsg.D7)
	#ret_check = libCAN.WriteCANMessage(handle, byref(pmsg))
	#time.sleep(0.5)
	#print rpm
	#print RPM
	#analogData.add(rpm)
        analogPlot.update(analogData)
#elif input == "loop":
"""
while True:
    if input == "normal":
        ret_check = libCAN.SetNormalMode(handle)
        if (ret_check == 0):
            print "Normal Mode Configured"
        else:
            print "Normal Mode  failed"
            #print ret_check
    #elif input == "write":
	printf("Send Value: %02X %02X %02X %02X %02X %02X %02X %02X %02X %02X %02X %02X %02X %02X %02X %02X\n",
		   pmsg.bExtended, pmsg.chTmStmpH, pmsg.chTmStmpL, pmsg.EArbId1, pmsg.EArbId0, pmsg.SArbId1, pmsg.SArbId0,
		   pmsg.DLC, pmsg.D0, pmsg.D1, pmsg.D2, pmsg.D3, pmsg.D4, pmsg.D5, pmsg.D6, pmsg.D7)
	ret_check = libCAN.WriteCANMessage(handle, byref(pmsg))
	time.sleep(0.5)
        #print ret_check
    elif input == "getbaud":
        GetBRate(handle, byref(Data))
        print
        Data.value
    elif input == "help":
        Help()
        time.sleep(0.2)
    elif input == "version":
        GetVer(handle, byref(Ver))
        print
        Ver.value
    elif input == "exit":
        sys.exit()
    else:
        print "Unknown Command!"
"""
