#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#       mirror.py
#       
#       Copyright 2011 ganesh <ganesh@debian>
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

import os,sys,commands
currentUser = commands.getoutput("whoami")
if currentUser != 'root':
    print "You need to be root!"
    sys.exit()
else:
	os.chdir('/etc/apt/')
	os.system('mv sources.list source.list.backup')
	os.system('touch source.list')
	source=	open("source.list", "w")
	for i in range(1,9):	
		source.write("deb http://192.168.1.114/dvd%s/debian/ squeeze main \n"%i)
	os.system('apt-get update')
