#! /usr/bin/env python

from os import fork, chdir, setsid, umask
from sys import exit
import serial,os
import time
import syslog


def main():
    port = "/dev/ttyUSB0"
    ser = serial.Serial(port, 9600, timeout=0)
    last_received = ''
    buffer = ''
    while 1:
        #main daemon process loop
        buffer += ser.read(ser.inWaiting())
        if '#' in buffer:
            last_received, buffer = buffer.split('#')[-2:]
            syslog.syslog('%s'%last_received)
            os.system("espeak '%s'"%last_received)



# Dual fork hack to make process run as a daemon
if __name__ == "__main__":
      try:
        pid = fork()
        if pid > 0:
          exit(0)
      except OSError, e:
        exit(1)

      chdir("/")
      setsid()
      umask(0)

      try:
        pid = fork()
        if pid > 0:
          exit(0)
      except OSError, e:
        exit(1)

main()
