import pygame
import sys

#Make a loop where the PI ( Angle of the arc ) constantly gets updated, like a crawling snake

pi = 3.14

screenX = 800
screenY = 600

speed = 0.15

arcY1 = 600
arcY2 = 600
arcY3 = 1200
arcY4 = 1200

#arc 1, 2 +10 / arc 2, 3 -582 / arc 3, 4 +12

pygame.init()
size = width, height = screenX, screenY
screen = pygame.display.set_mode(size)

while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()


    screen.fill((0,0,0))
  
    pygame.draw.arc(screen, (255, 0, 0), (screenX/5, arcY1, screenY-80, screenY+20), pi, 3*pi/2, 20)
    pygame.draw.arc(screen, (0, 255, 0), (screenX/5, arcY2, screenY-100, screenY+50), pi/2, pi, 20)
    pygame.draw.arc(screen, (0, 0, 255), (screenX/5, arcY3, screenY-100, screenY+20), 3*pi/2, 2*pi, 20)
    pygame.draw.arc(screen, (255, 165, 0), (screenX/5, arcY4, screenY-100, screenY+50), 0, pi/2, 20)

    arcY1 -= speed
    arcY2 -= speed
    arcY3 -= speed
    arcY4 -= speed

    if arcY1 < -600:
        arcY1 = 600

    if arcY2 < -600:
        arcY2 = 600

    if arcY3 < -600:
        arcY3 = 600

    if arcY4 < -600:
        arcY4 = 600

    pygame.display.flip()
