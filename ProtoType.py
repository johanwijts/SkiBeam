# Import Modules
import os
import pygame
import random
from pygame.locals import *
from pygame.compat import geterror

class Circle():
    def __init__(self, x):
        self.x = x
        self.y = -40
        self.w = 40
        self.h = 40
        self.v = 3

        self.slalom = 1

        self.is_left = True
        self.extra_clean = False
        self.random = False

    def update(self):
        self.y += self.v

    def clean_y(self):
        if self.extra_clean:
            return self.y - (self.v +1)
        else:
            return self.y - self.v

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
        self.y = 300

    def start_random(self):
        self.random = True
        self.set_random()

    def set_random(self):
        self.x = random.randint(0, 780)
        temp_y = random.randint(0, 600)
        self.y = temp_y * -1

    def set_slalom(self):
        if self.slalom > 2:
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
        

def main():
    """this function is called when the program starts.
       it initializes everything it needs, then runs in
       a loop until the function returns."""
# Initialize Everything
    pygame.init()
    screen = pygame.display.set_mode((800, 600))
    pygame.display.set_caption('SkiBeam')

# Create The Backgound
    screen.fill((255, 255, 255))
    pygame.display.update()

# Prepare Game Objects
    clock = pygame.time.Clock()
    allsprites = []

    updatesprites = []
    key_pressed = True

# Make 2 Circles
    for i in range(2):
        if (i % 2) == 0:
            circle = Circle(675)
            circle.is_right()
            circle.start_halfway()
            allsprites.append(circle)

        else:
            circle = Circle(100)
            allsprites.append(circle)
            
    
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
                    i.extra_clean_on()
                    i.slow_down()
                key_pressed = False

            elif event.key == pygame.K_LEFT and key_pressed:
                for i in allsprites:

                    i.set_slalom()
                    
                    if i.slalom == 1:
                        i.slalom_1()
                    elif i.slalom == 2:
                        i.slalom_2()
                    else:
                        i.slalom_3()

                screen.fill((255, 255, 255))
                pygame.display.update()
                        
                key_pressed = False
            
            elif event.key == pygame.K_RIGHT and key_pressed:
                for i in allsprites:
                    i.start_random()

                screen.fill((255, 255, 255))
                pygame.display.update()
                
                key_pressed = False

            elif event.key == pygame.K_a and key_pressed:
                return
        
            elif event.key == pygame.K_r and key_pressed:
                return

        if event.type == pygame.KEYUP:
            key_pressed = True

        #allsprites.update()

        # Draw Everything
        for i in allsprites[:]:
            pygame.draw.rect(screen, (255, 255, 255), (i.x, i.clean_y(), i.w, i.h))
            updatedirty = pygame.Rect((i.x, i.clean_y(), i.w, i.h))
            pygame.draw.rect(screen, (255, 0, 0), (i.x, i.y, i.w, i.h))
            updateclean = pygame.Rect((i.x, i.y, i.w, i.h))

            updatesprites.append(updatedirty)
            updatesprites.append(updateclean)

            if i.extra_clean:
                i.extra_clean_off()

            if i.random:
                if (len(allsprites) < 8):
                    circle = Circle(0)
                    circle.start_random()
                    allsprites.append(circle)
            
            if i.y > 600:
                if i.random:
                    allsprites.remove(i)

                else:
                    i.y = -40
            
            i.update()
        
        clock.tick(120)
        pygame.display.update(updatesprites)
        updatesprites.clear()

    pygame.quit()

# this calls the 'main' function when this script is executed
if __name__ == '__main__':
    main()

