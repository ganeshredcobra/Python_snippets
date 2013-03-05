#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#       serial_read.py
#
#       Copyright 2011 ganesh <ganeshredcobra@gmail.com>
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
        #os.system(' echo \'(voice_en1_mbrola)(SayText "%s")\' | festival'%last_received)
