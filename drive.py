import pygame
import subprocess
import datetime
import os

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
    for i in range(axes):
        axis = joystick.get_axis(i)
        #print("Axis {} value: {}".format(i, axis))

