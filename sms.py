#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#       sms.py
#       
#       Copyright 2013 Ganesh <ganeshredcobra@gmail.com>
#       
#       This program is free software; you can redistribute it and/or modify
#       it under the terms of the GNU General Public License as published by
#       the Free Software Foundation; either version 2 of the License, or
#       (at your option) any later version.
#       
#       This program is distributed in the hope that it will be useful,
#       but WITHOUT ANY WARRANTY; without even the implied warranty of
#       MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#       GNU General Public License for more details.
#       
#       You should have received a copy of the GNU General Public License
#       along with this program; if not, write to the Free Software
#       Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
#       MA 02110-1301, USA.


import serial
 
# Set up the connection to the dongle
dongle = serial.Serial(port="/dev/ttyUSB0",baudrate=115200,timeout=0,rtscts=0,xonxoff=0)
 
# This sends the command to the dongle
def sendatcmd(cmd):
    dongle.write('AT'+cmd+'\r')
 
# put the dongle into text mode
sendatcmd('+CMGF=1')
 
# Set the telephone number we want to send to
sendatcmd('+CMGS="+91********"')
 
# Set the message we want to send
dongle.write('Sending from python')
 
# Pass the CTRL+Z character to let the dongle know we're done
dongle.write(chr(26))
 
# Close the connection
dongle.close()
