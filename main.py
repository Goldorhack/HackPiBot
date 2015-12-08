import sys
import RPi.GPIO as GPIO
from time import sleep
from RPIO import PWM
from move_function import *

init_pos()

to_top()

sleep(2)
