#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#       copy.py
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

from __future__ import print_function
import glob
import re
import os
import subprocess

# Add any other device pattern to read from
dev_pattern = ['sd.*','mmcblk*']

def size(device):
    nr_sectors = open(device+'/size').read().rstrip('\n')
    sect_size = open(device+'/queue/hw_sector_size').read().rstrip('\n')

    # The sect_size is in bytes, so we convert it to GiB and then send it back
    return (float(nr_sectors)*float(sect_size))/(1024.0*1024.0*1024.0)

"""def detect_devs():
    for device in glob.glob('/sys/block/*'):
        for pattern in dev_pattern:
            if re.compile(pattern).match(os.path.basename(device)):
                print('Device:: {0}, Size:: {1} GiB'.format(device, size(device)))"""
                
def detect_devs():
    First_SZ = subprocess.check_output('du -skh First', shell=True)
    Second_SZ = subprocess.check_output('du -skh Second', shell=True)
                
def detect_devs():
    #os.system('lsblk -n -o MOUNTPOINT|grep media')
    procd = subprocess.check_output('lsblk -n -o MOUNTPOINT|grep media', shell=True)
    #print (procd)
    First=procd.splitlines()[0]
    Second=procd.splitlines()[1]
    print (First)
    print (Second)
    First_SZ = subprocess.check_output('du -sk %s'%First, shell=True)
    Second_SZ = subprocess.check_output('du -sk %s'%Second, shell=True)
    F_SZ=First_SZ.split()[0]
    S_SZ=Second_SZ.split()[0]
    print (F_SZ)
    print (S_SZ)
    if (int(F_SZ) > int(S_SZ)):
        print ("F_SZ is bigger")
    else:
        print ("S_SZ is bigger")
    Sor = subprocess.check_output('zenity --entry --title "Select Flash Drives" --text "Select Source Drive." %s %s'%(First,Second), shell=True)
    Des = subprocess.check_output('zenity --entry --title "Select Flash Drives" --text "Select Destination Drive." %s %s'%(First,Second), shell=True)
    print (Sor)
    print (Des)

if __name__=='__main__':
    detect_devs()
