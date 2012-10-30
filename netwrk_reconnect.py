#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#       network.py
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



import urllib2
import time
import os,sys

count=1
output=0
def internet_on():	
    try:
        response=urllib2.urlopen('http://google.com',timeout=1)
        output=1
        print output
        if output==1:
            print "ok"
    except:
        print "nm restarted"
        os.system('/etc/init.d/network-manager restart')
        time.sleep(40)
if __name__ == '__main__':	
    while count!=0:
        internet_on()
        print "loop"
        time.sleep(5)

