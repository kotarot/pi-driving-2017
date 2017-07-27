import pygame
import subprocess
import datetime
import os
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

basepath = os.path.abspath(os.path.dirname(__file__))

pygame.init()

pygame.joystick.init()
joystick = pygame.joystick.Joystick(0)
pygame.joystick.Joystick(0).init()

while  True:
    for event in pygame.event.get():
        if event.type == pygame.JOYBUTTONDOWN:
            print(event.__dict__)
            todaydetail = datetime.datetime.today()
            cmd = ''
            if event.__dict__['button'] == 0:
                cmd = "raspistill -o '" + basepath + "/images/image_" + str(todaydetail) + ".jpg' -t 1 -n"
            elif event.__dict__['button'] == 1:
                cmd = "raspistill -o '" + basepath + "/images/image_" + str(todaydetail) + ".jpg' -t 1 -n -ifx gpen"
            if cmd != '':
                subprocess.call(cmd,shell=True)
        if event.type == pygame.JOYBUTTONUP:
            print(event.__dict__)

    hat = joystick.get_hat(0)
    #print("Hat {} value: {}".format(0, str(hat)))

    axes = joystick.get_numaxes()
    #for i in range(axes):
    #    axis = joystick.get_axis(i)
    #    print("Axis {} value: {}".format(i, axis))
    left = joystick.get_axis(1)
    right = joystick.get_axis(5)
    print(left, right)

    if right<-0.9:
        GPIO.output(PIN1, True)
        GPIO.output(PIN2, False)
    elif right>0.9:
        GPIO.output(PIN1, False)
        GPIO.output(PIN2, True)
    else:
        GPIO.output(PIN1, False)
        GPIO.output(PIN2, False)
    if left<-0.9:
        GPIO.output(PIN3, True)
        GPIO.output(PIN4, False)
    elif left>0.9:
        GPIO.output(PIN3, False)
        GPIO.output(PIN4, True)
    else:
        GPIO.output(PIN3, False)
        GPIO.output(PIN4, False)
