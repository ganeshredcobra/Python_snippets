#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#       set_dwnld_limit.py
#
#       Copyright 2011 ganesh <ganesh@space-kerala.org>
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

import os,sys

def change():
	s=line[1027]
	n=s.split()
	val=raw_input("Enter Download Limit in MB: ")
	n[1]=val
	new=" ".join(n)
	#print(new)
	f.close()
	fi=open('%s'%PATH)
	files=fi.read()
	#print(files)
	text=files.replace('%s'%s,'%s \n'%new)
	#print(text)
	fil=open('%s'%PATH,'w+')
	fil.write('%s'%text)

def status():
	s=line[1027]
	n=s.split()
	print('The current Download Limit is %s MB'%n[1])
	f.close()

def restart():
	os.system('service squid3 restart')

if os.geteuid()!=0:
    sys.exit("\nPlease  run this utility as root\n")
else:
	var=raw_input("1.Check current Download Limit \n2.Change Download Limit \n Enter your Option :")
	PATH="/etc/squid3/squid.conf"
	f=open('%s'%PATH)
	line=f.readlines()
	if "1" in var:
		status()
		res=raw_input("Do you want to change download limit[y/n] :")
		if "y" in res:
			change()
			restart()
		else:
			sys.exit()
	else:
		change()
		restart()

