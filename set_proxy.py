#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#       set_proxy.py
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

import os
import sys
import getpass
import commands

flag=False
def idenos():
	raw=commands.getoutput('lsb_release -d').split()
	#print(raw[1])
	return raw[1]

def temp_write():
	commands.getoutput("touch /tmp/tmp_proxy")
	#os.seteuid(0)
	f = open('/tmp/tmp_proxy','w')
	if (proxy[0]==True):
		f.write('Acquire::http::proxy "'+proxy[1]+'";\n')
		f.write('Acquire::ftp::proxy "'+proxy[2]+'";\n')
		f.write('Acquire::https::proxy "'+proxy[3]+'";\n')
		f.close()
		return
	else:
		f.write('Acquire::http::proxy "'+proxy[1]+'";\n')
		f.close()
		return

def datas():
	host = raw_input("Enter Proxy Host: ")
	port = raw_input("Enter Proxy Port: ")
	auth = raw_input("Does the proxy need authentication[y/n]: ")
	if 'y' in auth:
		user = raw_input("Enter Username: ")
		passw = getpass.getpass("Enter Password: ")
		proxyline = user +':' + passw + '@'
		proxyline = proxyline + host + ':' + port + '/'
		print proxyline
		prot = raw_input("Is the proxy for all protocols (otherwise only http will be set)[y/n]: ")
		if 'y' in prot:
			flag=True
			http_proxy = 'http://'+proxyline
			https_proxy = 'https://'+proxyline
			ftp_proxy = 'ftp://'+proxyline
			return flag,http_proxy,https_proxy,ftp_proxy

		else:
			http_proxy = 'http://'+proxylineproxyline
			return flag,http_proxy


if os.geteuid()!=0:
    sys.exit("\nPlease  run this utility as root\n")
else:
	var = raw_input("Do you want to set proxy[y/n]: ")
	if "y" in var:
		os=idenos()
		if(os=="Debian"):
			proxy=datas()
			temp_write()
			commands.getoutput("cp /etc/apt/apt.conf.d/99synaptic /etc/apt/apt.conf.d/99synaptic.bak")
			commands.getoutput("cat /tmp/tmp_proxy >> /etc/apt/apt.conf.d/99synaptic")
			commands.getoutput("apt-get update")
			print "Job Completed"
        elif(os=="Ubuntu"):
            proxy=datas()
            temp_write()
            commands.getoutput("cp /etc/apt/apt.conf /etc/apt/apt.conf.bak")
            commands.getoutput("cat /tmp/tmp_proxy >> /etc/apt/apt.conf")
            print "Job Completed"







