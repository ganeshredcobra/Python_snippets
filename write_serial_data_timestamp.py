#! /usr/bin/env python
#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#       write_serial_data_timestamp.py
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

import os,sys,serial,commands
from datetime import datetime
currentUser = commands.getoutput("whoami")


def timestamp():
	FORMAT = '%Y-%m-%d-%H-%M-%S'
	STAMP = '%s' % (datetime.now().strftime(FORMAT))
	return STAMP


if __name__=='__main__':
    if currentUser != 'root':
        print "You need to be root!"
        sys.exit()
    else:        
        ser = serial.Serial("/dev/ttyUSB0", 9600, timeout=1)        
        while True:
            data=ser.readline()
            TIME=timestamp()
            if data!='':
                file=open('/var/www/serial.txt','a')
                file.write('%s: '%TIME+data+'\n')
                #print TIME



