import sys
import RPi.GPIO as GPIO
from time import sleep
from RPIO import PWM

pos_file_x = "./pos_x.txt"
pos_file_y = "./pos_y.txt"

GPIO.setmode(GPIO.BCM)

GPIO.setup(22,GPIO.OUT)
GPIO.setup(4,GPIO.OUT)

PWM.setup()
PWM.init_channel(0)

# GPIO 22 = pos_x gauche-droite = 100 (150) 200
# GPIO 4 = pos_y bas-haut = 150 (200) 250

pos_x = 0
pos_y = 0
step = 15

def init_pos():
	
        PWM.add_channel_pulse(0, 4, 0, 198)
        PWM.add_channel_pulse(0, 22, 0, 148)
	sleep(2)

def read_pos():
	global pos_y
	global pos_file_x
	global pos_file_y
	global pos_x
	pos = open(pos_file_x,"r")
        pos_x = pos.read()
        pos.close()
	pos = open(pos_file_y,"r")
        pos_y = pos.read()
        pos.close()

def to_right():
	global pos_x
	global step
	read_pos()
	pos_x = int(pos_x) - int(step)
	pos = open(pos_file_x,"w")
	pos.write(str(pos_x))
	pos.close()
	PWM.add_channel_pulse(0, 22, 0, pos_x)
	sleep(1)

def to_left():
        global pos_x
	global step
        read_pos()
        pos_x = int(pos_x) + int(step)
        pos = open(pos_file_x,"w")
        pos.write(str(pos_x))
        pos.close()
        PWM.add_channel_pulse(0, 22, 0, pos_x)
	sleep(1)

def to_top():
        global pos_y
	global step
        read_pos()
        pos_y = int(pos_y) - int(step)
        pos = open(pos_file_y,"w")
        pos.write(str(pos_y))
        pos.close()
        PWM.add_channel_pulse(0, 4, 0, pos_y)
	sleep(1)

def to_bottom():
        global pos_y
	global step
        read_pos()
        pos_y = int(pos_y) + int(step)
        pos = open(pos_file_y,"w")
        pos.write(str(pos_y))
        pos.close()
        PWM.add_channel_pulse(0, 4, 0, pos_y)
	sleep(1)
