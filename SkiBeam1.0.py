import pygame
import random
pygame.init()

xScreenSet = 0
yScreenSet = 0
import os
os.environ['SDL_VIDEO_WINDOW_POS'] = "%d,%d" % (xScreenSet,yScreenSet)

win = pygame.display.set_mode((1920, 1280))

pygame.display.set_caption("SkiBeam1.0")


class Pylon:

    def __init__(self, x, y, w, h):
        self.x = x
        self.y = y
        self.w = w
        self.h = h

        self.v = 0

    def get_x(self, x):
        return self.x

    def get_y(self, y):
        return self.y

    def up_v(self):
        self.v += 1

    def down_v(self):
        self.v -= 1

    def reset_y(self, y):
        self.y = y

p1 = Pylon(480, 0, 50, 0)
p2 = Pylon(1440, 0, 50, 0)

clock = pygame.time.Clock()

circles = []

key_pressed = True
random_active = False

run = True
while run:
    dt = clock.tick(100)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_ESCAPE:
            run = False

        elif event.key == pygame.K_UP and key_pressed:
            p1.up_v()
            p2.up_v()
            key_pressed = False

        elif event.key == pygame.K_DOWN and key_pressed:
            p1.down_v() 
            p2.down_v()
            key_pressed = False

        elif event.key == pygame.K_LEFT and key_pressed:
            p1.x -= 3
            p2.x += 3      
            
        elif event.key == pygame.K_RIGHT and key_pressed:
            p1.x += 3
            p2.x -= 3

        elif event.key == pygame.K_a and key_pressed:
            p2.y += 3
        
        elif event.key == pygame.K_r and key_pressed:
            if random_active == False:
                random_active = True
                key_pressed = False
                print (random_active)

            else:
                random_active = False
                key_pressed = False
            

    if event.type == pygame.KEYUP:
        key_pressed = True

    p1.y += p1.v
    p2.y += p2.v

    if random_active:
        if p1.y > 1280:
            p1.x = random.randint(50, 1870)

        if p2.y > 1280:
            p1.x = random.randint(50, 1870)
    
    if p1.y > 1280:
        p1.y = 0

    if p2.y > 1280:
        p2.y = 0

    win.fill((255, 255, 255))
    
    circle1 = pygame.draw.circle(win, (255, 255, 255), (p1.x, p1.y), p1.w, p1.h)
    circle2 = pygame.draw.circle(win, (255, 255, 255), (p1.x, p1.y), p1.w, p1.h)
    circles.append(circle1)
    circles.append(circle2)
    
    pygame.draw.circle(win, (255, 0, 0), (p1.x, p1.y), p1.w, p1.h)
    pygame.draw.circle(win, (255, 0, 0), (p2.x, p2.y), p2.w, p2.h)
    pygame.display.update(circles)

pygame.quit()
