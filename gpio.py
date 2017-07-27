#!/usr/bin/env python2

import RPi.GPIO as GPIO

PIN1 = 31 #right
PIN2 = 33 #right
PIN3 = 35 #left
PIN4 = 37 #left

GPIO.setmode(GPIO.BOARD)
GPIO.setup(PIN1,GPIO.OUT)
GPIO.setup(PIN2,GPIO.OUT)
GPIO.setup(PIN3,GPIO.OUT)
GPIO.setup(PIN4,GPIO.OUT)


GPIO.output(PIN1, True)
GPIO.output(PIN2, False)
GPIO.output(PIN3, False)
GPIO.output(PIN4, False)

