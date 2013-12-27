import string
import ctypes
from ctypes import *

#C:\WINDOWS\system32\CANMateDll.dll

hllDll = ctypes.WinDLL ("C:\WINDOWS\system32\CANMateDll.dll")
handle=c_int(1)
Datacalbk=c_void_p(1)
Eventcalbk=c_void_p(1)


while True:
    input = raw_input("Enter the command : ")
    if input == "open":
        handle = hllDll.OpenCANMate(Datacalbk,Eventcalbk)
        print handle
    elif input == "close":
        hllDll.CloseCANMate(handle)