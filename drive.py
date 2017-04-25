import pygame

pygame.init()

pygame.joystick.init()
joystick = pygame.joystick.Joystick(0)
pygame.joystick.Joystick(0).init()

while  True:
    for event in pygame.event.get():
        if event.type == pygame.JOYBUTTONDOWN:
            print(event.__dict__)
        if event.type == pygame.JOYBUTTONUP:
            print(event.__dict__)

    hat = joystick.get_hat(0)
    print("Hat {} value: {}".format(0, str(hat)))

    axes = joystick.get_numaxes()
    for i in range(axes):
        axis = joystick.get_axis(i)
        print("Axis {} value: {}".format(i, axis))

