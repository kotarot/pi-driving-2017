#!/usr/bin/env python2

import RPi.GPIO as GPIO

PIN1 = 31
PIN2 = 33
PIN3 = 35
PIN4 = 37

GPIO.setmode(GPIO.BOARD)
GPIO.setup(PIN1,GPIO.OUT)
GPIO.setup(PIN2,GPIO.OUT)
GPIO.setup(PIN3,GPIO.OUT)
GPIO.setup(PIN4,GPIO.OUT)

GPIO.output(PIN1, False)
GPIO.output(PIN2, False)
GPIO.output(PIN3, False)
GPIO.output(PIN4, False)

