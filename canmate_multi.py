import platform
import time,sys
import ctypes
from ctypes import *

PLATFORM = platform.system()
if PLATFORM == "Windows":
	from ctypes.wintypes import *
	libCAN =  ctypes.WinDLL ("C:\WINDOWS\system32\CANMateDll.dll")
else:
	libCAN = cdll.LoadLibrary("./libCANMATE.so")


# Define the CAN Message struct
class CANMsg(Structure):
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

#Datacallback function
def Datacalbk(a, b):
   print "Received: "
   print a[0].bExtended,a[0].chTmStmpH,a[0].chTmStmpL,a[0].EArbId1,a[0].EArbId0,a[0].SArbId1,a[0].SArbId0,a[0].DLC,a[0].D0,a[0].D1,a[0].D2,a[0].D3,a[0].D4,a[0].D5,a[0].D6,a[0].D7
   #print "Hello\n"
   return 0

#Eventcallback function
def Eventcalbk(a):
   print "Event Occured\n"
   print a[0].chErr,a[0].chTxErrCnt,a[0].chRxErrCnt
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
chBaudRate =c_int(9) #BAUD_RATE500K	9 

pmsg = CANMsg(0,0,0,0,0,0,8,2,1,2,3,4,5,6,7,8) #  initially memset to {0}
libCAN.WriteCANMessage.argtypes = [handle, POINTER(CANMsg)]

#Datacallback and Eventcallback function declaration
DataCB = CFUNCTYPE(c_int,POINTER(CANMsg) ,POINTER(c_int))
EventCB = CFUNCTYPE(c_int,POINTER(CANEvent))
_data_fn = DataCB(Datacalbk)
_event_fn = EventCB(Eventcalbk)

libCAN.OpenCANMate.argtypes = [DataCB , EventCB]

#GetBaudRate function declaration
GetBRate = libCAN.GetCurrentBaudRate
GetBRate.restype = c_int
GetBRate.argtypes = [handle, POINTER(c_int)]
Data = c_int()

#GetFirmware Version
GetVer = libCAN.GetFirmwareVersion
GetVer.restype = c_int
GetVer.argtypes = [handle, POINTER(c_int)]
Ver= c_int()

Help()
while True:
    input = raw_input("Enter the command : ")
    if input == "open":
        handle = libCAN.OpenCANMate( _data_fn, _event_fn)
        #print handle
        if(handle > 0):
           print "Open Sucess"
        else:
          print "Error Opening"
    elif input == "close":
        libCAN.CloseCANMate(handle)
        print "CANMate closed"
    elif input == "setbaud":
        ret_check = libCAN.SetCANBaudRate(handle, chBaudRate)
        if(ret_check == 0):
           print "CAN Baudrate of 500K Configured"
        else:
           print "CAN Baudrate Config failed"
        #print ret_check
    elif input == "recep":
        ret_check = libCAN.StartReception(handle)
        if(ret_check == 0):
           print "Reception Started"
        else:
           print "Reception failed"
        #print ret_check
    elif input == "loop":
        ret_check = libCAN.SetLoopbackMode(handle)
        if(ret_check == 0):
           print "Loop Back Mode Configured"
        else:
           print "Loop Back Mode  failed"
        #print ret_check
    elif input == "normal":
        ret_check = libCAN.SetNormalMode(handle)
        if(ret_check == 0):
           print "Normal Mode Configured"
        else:
           print "Normal Mode  failed"
        #print ret_check
    elif input == "write":
        print "Send Value"
        print pmsg.bExtended,pmsg.chTmStmpH,pmsg.chTmStmpL,pmsg.EArbId1,pmsg.EArbId0,pmsg.SArbId1,pmsg.SArbId0,pmsg.DLC,pmsg.D0,pmsg.D1,pmsg.D2,pmsg.D3,pmsg.D4,pmsg.D5,pmsg.D6,pmsg.D7
        ret_check = libCAN.WriteCANMessage(handle, byref(pmsg))
        time.sleep(0.5)
        #print ret_check
    elif input == "getbaud":
        GetBRate(handle, byref(Data))
        print Data.value
    elif input == "help":
        Help()
        time.sleep(0.2)
    elif input == "version":
        GetVer(handle, byref(Ver))
        print Ver.value
    elif input == "exit":
         sys.exit()
    else:
       print "Unknown Command!"
