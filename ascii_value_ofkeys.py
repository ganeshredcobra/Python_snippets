#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#       untitled.py
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

# KeyLogger.py
# show a character key when pressed without using Enter key
# hide the Tkinter GUI window, only console shows

#!/usr/bin/env python

#keystroke.py

loop = True

import curses

print "This is the first line"
print "This is the second line"
print "This is the third line"


stdscr = curses.initscr()


curses.noecho()
curses.cbreak()

while loop:
    c = stdscr.getch(0,0)
    d = c-48
    print d


curses.nocbreak()
curses.echo()
curses.endwin()  
