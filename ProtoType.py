# Import Modules
import os
import pygame
import random
from pygame.locals import *
from pygame.compat import geterror

class Shape():
    def __init__(self, x, screenX, screenY):
        self.x = x
        self.y = 600
        self.w = 40
        self.h = 40
        self.v = 2

        self.screenXpos = screenX
        self.screenYpos = screenY

        self.slalom = 1

        self.is_left = True
        self.extra_clean = False

    def update(self):
        self.y -= self.v

    def clean_y(self):
        if self.extra_clean:
            return self.y + (self.v +3)
        else:
            return self.y + self.v

    def extra_clean_on(self):
        self.extra_clean = True

    def extra_clean_off(self):
        self.extra_clean = False

    def speed_up(self):
        self.v += 1
        self.h += 1

    def slow_down(self):
        self.v -= 1
        self.h -= 1

    def widen_up(self):
        self.x -= 5

    def narrow_down(self):
        self.x += 5

    def is_right(self):
        self.is_left = False
        
    def start_halfway(self):
        self.y = 260

    def set_random(self):
        self.x = random.randint(0, 780)
        self.y = random.randint(600, 900)

    def set_slalom(self):
        if self.slalom > 3:
            self.slalom = 1
        else:
            self.slalom += 1

    def slalom_1(self):
        if self.is_left:
            self.x = 100
        else:
            self.x = 675

    def slalom_2(self):
        if self.is_left:
            self.x = 200
        else:
            self.x = 575

    def slalom_3(self):
        if self.is_left:
            self.x = 300
        else:
            self.x = 475

    def slalom_4(self):
        self.x = 400

class Square(Shape):
    pass

class Arc():
    pass

def main():
    """this function is called when the program starts.
       it initializes everything it needs, then runs in
       a loop until the function returns."""
# Initialize Everything
    pygame.init()
    screenX = 800
    screenY = 600
    screen = pygame.display.set_mode((screenX, screenY))
    pygame.display.set_caption('SkiBeam')

# Create The Backgound
    screen.fill((0, 0, 0))
    pygame.display.update()

# Prepare Game Objects
    clock = pygame.time.Clock()
    allsprites = []

    updatesprites = []
    key_pressed = True
    random_mode = False

# Make 2 Squares
    for i in range(2):
        if (i % 2) == 0:
            square = Square(0.8*screenX-40, screenX, screenY)
            square.is_right()
            square.start_halfway()
            allsprites.append(square)

        else:
            square = Square(0.2*screenX, screenX, screenY)
            allsprites.append(square)
            
    
    print("Lets go")

# Main Loop
    going = True
    while going:
        
        # Handle Input Events
        for event in pygame.event.get():
            if event.type == QUIT:
                going = False
            
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                going = False
            
            elif event.key == pygame.K_UP and key_pressed:
                for i in allsprites:
                    i.speed_up()
                key_pressed = False

            elif event.key == pygame.K_DOWN and key_pressed:
                for i in allsprites:
                    if i.v > 0:
                        i.extra_clean_on()
                        i.slow_down()
                key_pressed = False

            elif event.key == pygame.K_RIGHT and key_pressed:
                for i in allsprites:

                    i.set_slalom()
                    
                    if i.slalom == 1:
                        i.slalom_1()
                    elif i.slalom == 2:
                        i.slalom_2()
                    elif i.slalom == 3:
                        i.slalom_3()
                    else:
                        i.slalom_4()

                screen.fill((0, 0, 0))
                pygame.display.update()
                        
                key_pressed = False

        if event.type == pygame.KEYUP:
            key_pressed = True

        #allsprites.update()

        # Draw Everything
        for i in allsprites[:]:
            pygame.draw.rect(screen, (0, 0, 0), (i.x, i.clean_y(), i.w, i.h))
            updatedirty = pygame.Rect((i.x, i.clean_y(), i.w, i.h))
            pygame.draw.rect(screen, (255, 0, 0), (i.x, i.y, i.w, i.h))
            updateclean = pygame.Rect((i.x, i.y, i.w, i.h))

            updatesprites.append(updatedirty)
            updatesprites.append(updateclean)

            if i.extra_clean:
                i.extra_clean_off()
            
            if i.y < -100:
                i.y = screenY
            
            i.update()
        
        clock.tick(120)
        pygame.display.update(updatesprites)
        updatesprites.clear()

    pygame.quit()

# this calls the 'main' function when this script is executed
if __name__ == '__main__':
    main()

