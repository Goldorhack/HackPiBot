import sys
import os
import RPi.GPIO as GPIO
from time import sleep
from RPIO import PWM
from move_function import *

#pos_x = 0
#pos_y = 0
#step = 20

#sys.argv[1]()
#to_bottom()
#os.system(sys.argv[1]+'()')

#arg = sys.argv[1].lower()
#arg()

if(sys.argv[1] == 'init_pos'):
	init_pos()
if(sys.argv[1] == 'to_right'):
	to_right()
if(sys.argv[1] == 'to_left'):
	to_left()
if(sys.argv[1] == 'to_top'):
	to_top()
if(sys.argv[1] == 'to_bottom'):
	to_bottom()
