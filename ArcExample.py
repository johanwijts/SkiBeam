import pygame
import sys
from pygame.locals import *
from pygame.compat import geterror

pi = 3.14

screenX = 800
screenY = 600

speed = 0.15

arcY1 = 600
arcY2 = 600
arcY3 = 1200
arcY4 = 1200

arcXpos = screenX

arcW1 = screenY
arcW2 = screenY
arcW3 = screenY
arcW4 = screenY

going = True

pygame.init()
size = width, height = screenX, screenY
screen = pygame.display.set_mode(size)

key_pressed = True

while going:
    # Handle Input Events
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                going = False
        
            elif event.key == pygame.K_UP and key_pressed:
                speed += 0.01
                key_pressed = False

            elif event.key == pygame.K_DOWN and key_pressed:
                if speed > 0:
                    speed -= 0.01
                    key_pressed = False

            elif event.key == pygame.K_RIGHT and key_pressed:
                arcW1 += 10
                arcW2 += 10
                arcW3 += 10
                arcW4 += 10

                arcXpos -= 27
                
                key_pressed = False

            elif event.key == pygame.K_LEFT and key_pressed:
                arcW1 -= 10
                arcW2 -= 10
                arcW3 -= 10
                arcW4 -= 10

                arcXpos += 27
                
                key_pressed = False

        if event.type == pygame.KEYUP:
            key_pressed = True


    screen.fill((0,0,0))
  
    pygame.draw.arc(screen, (255, 0, 0), (arcXpos/5, arcY1, arcW1-80, screenY+20), pi, 3*pi/2, 20)
    pygame.draw.arc(screen, (0, 255, 0), (arcXpos/5, arcY2, arcW2-100, screenY+50), pi/2, pi, 20)
    pygame.draw.arc(screen, (0, 0, 255), (arcXpos/5, arcY3, arcW3-100, screenY+20), 3*pi/2, 2*pi, 20)
    pygame.draw.arc(screen, (255, 165, 0), (arcXpos/5, arcY4, arcW4-100, screenY+50), 0, pi/2, 20)

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
pygame.quit()
