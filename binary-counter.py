#!/usr/bin/env python
#
# A binary counter example to demo the disp_bin function, which takes a number
# and 2 hex RGB values (for zero and one) and displays the number in binary on a
# Pimoroni Blinkt! shim.  
#
#

import time
from sys import exit
import blinkt

blinkt.set_clear_on_exit()

# Convert a hex colour to an RGB tuple.
def hex_to_rgb(col_hex):
    col_hex = col_hex.lstrip("#")
    return bytearray.fromhex(col_hex)

def disp_bin(num,zcolor,ocolor):
	# set the mask
	mask = 1
	# check the status of each bit in the number
	for i in range (0,8):
		# if the bit is 0, set r,g,b to the colors for 0
		if num & mask == 0:
			r, g, b = hex_to_rgb(zcolor)
		# otherwise use the colors for 1
		else:
			r, g, b = hex_to_rgb(ocolor)
		# shift the mast one bit to the left
		mask = mask << 1
		# set the appropriate pixel
		blinkt.set_pixel(i,r,g,b)
	# display the pixels
	blinkt.show()
	return	
	
for i in range (0,256):
	print (i)
	disp_bin(i,"001100","000011")
	time.sleep(0.1)
time.sleep(1)

