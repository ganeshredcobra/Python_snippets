#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#       mount.py
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
path= os.path.realpath(os.path.expanduser('~'+"/images"))
currentUser = commands.getoutput("whoami")
if currentUser != 'root':
    print "You need to be root!"
    sys.exit()
else:
	os.chdir('%s'%path)
	for i in range(1,9):
		os.system('mount debian-6.0.0-i386-DVD-%s.iso /media/dvd%s -o loop'%(i,i))
		os.system('ln -s /media/dvd%s/ /var/www/'%i)
