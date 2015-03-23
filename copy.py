#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#       copy.py
#
#       Copyright 2015 ganesh <ganeshredcobra@gmail.com>
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
    #os.system('lsblk -n -o MOUNTPOINT|grep media')
    procd = subprocess.check_output('lsblk -n -o MOUNTPOINT|grep media', shell=True)
    #print (procd)
    First=procd.splitlines()[0]
    Second=procd.splitlines()[1]
    #print (First)
    #print (Second)
    Sorz = subprocess.check_output('zenity --entry --title "Select Flash Drives" --text "Select Source Drive." %s %s'%(First,Second),       shell=True)
    Desz = subprocess.check_output('zenity --entry --title "Select Flash Drives" --text "Select Destination Drive." %s %s'%(First,Second), shell=True)
    #print ("Source is "+Sorz)
    #print ("Destination is "+Desz)

    Sorz_SZ_RW = subprocess.check_output('df -m %s'%Sorz, shell=True)
    Desz_SZ_RW = subprocess.check_output('df -m %s'%Desz, shell=True)
    Sorz_SZ=Sorz_SZ_RW.splitlines()[1].split()[2]
    Desz_SZ=Desz_SZ_RW.splitlines()[1].split()[3]
    #print ("Free space in MB %s for"%Sorz+" "+ Sorz_SZ)
    #print ("Free space in MB %s for"%Desz+" "+ Desz_SZ)
    if (int(Sorz_SZ) > int(Desz_SZ)):
        #print ("Not enough space in destination")
        subprocess.check_output('zenity --error --text "Not enough space in Destination! "',shell=True)
    else:
        #print ("Copying :)")
        #print ("Source is "+Sorz)
        #print ("Destination is "+Desz)
        Sorz_nl=Sorz+"/*"
        Sorz_star=Sorz_nl.split()[0]+Sorz_nl.split()[1]
        #print ("Destination is %s"%Desz)
        #print ("Source * is %s"%Sorz_star)
        One=Sorz_star.strip()
        Two=Desz.strip()
        subprocess.call('cp -R %s %s |zenity --progress --text "Copying" --pulsate --auto-close'%(One,Two), shell=True)
        subprocess.check_output('zenity --info --text "Copying complete"',shell=True)
  
if __name__=='__main__':
    detect_devs()
