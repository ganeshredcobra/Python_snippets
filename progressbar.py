#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# ascii command-line progress bar with percentage and elapsed time display
#
# adapted from Pylot source code (original by Vasil Vangelovski)
# modified and adapted by yudha gunslinger_ - 2010

import sys,time

class ProgressBar:
 def __init__(self, duration):
	 self.duration = duration
	 self.prog_bar = '[]'
	 self.fill_char = '#'
	 self.width = 100
	 self.__update_amount(0)

 def __update_amount(self, new_amount):
	 percent_done = int(round((new_amount / 100.0) * 100.0))
	 all_full = self.width - 2
	 num_hashes = int(round((percent_done / 100.0) * all_full))
	 self.prog_bar = '[' + self.fill_char * num_hashes + ' ' * (all_full - num_hashes) + ']'
	 pct_place = (len(self.prog_bar) / 2) - len(str(percent_done))
	 pct_string = '%i%%' % percent_done
	 self.prog_bar = self.prog_bar[0:pct_place] + \
	 (pct_string + self.prog_bar[pct_place + len(pct_string):])

 def update_time(self, elapsed_secs):
	 self.__update_amount((elapsed_secs / float(self.duration)) * 100.0)
	 self.prog_bar += '  %ds/%ss' % (elapsed_secs, self.duration)

 def __str__(self):
	return str(self.prog_bar)

if __name__ == '__main__':
	for a in range (61):
		 p = ProgressBar(60) # per 1 minute
		 p.update_time(a)
		 sys.stdout.write ("\r%s" % p)
		 sys.stdout.flush()
		 time.sleep(1)
		 a += 1
	else:
		 print "\n"
		 print " That's all, folks !"
		 print " Enjoy :)"

#    p.fill_char = '='
#    p.update_time(30) # 1/2 minute
#    print p

#    p.fill_char = '~'
#    p.update_time(60) # 1 minute
#    print p

