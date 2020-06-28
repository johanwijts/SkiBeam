# Import Modules
import os
import pygame
from pygame.locals import *
from pygame.compat import geterror

class Circle():
    def __init__(self, x):
        self.x = x
        self.y = 0
        self.w = 30
        self.h = 30
        self.v = 3

    def update(self):
        self.y += self.v

    def clean(self):
        return self.y - self.v

    def start_halfway(self):
        self.y = 300
        

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

# Make 2 Circles
    for i in range(2):
        if (i % 2) == 0:
            circle = Circle(675)
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
            elif event.type == KEYDOWN and event.key == K_ESCAPE:
                going = False

        #allsprites.update()

        # Draw Everything
        for i in allsprites:
            pygame.draw.rect(screen, (255, 255, 255), (i.x, i.clean(), i.w, i.h))
            updatedirty = pygame.Rect((i.x, i.clean(), i.w, i.h))
            pygame.draw.rect(screen, (255, 0, 0), (i.x, i.y, i.w, i.h))
            updateclean = pygame.Rect((i.x, i.y, i.w, i.h))

            updatesprites.append(updatedirty)
            updatesprites.append(updateclean)

            if i.y > 600:
                i.y = 0
            
            i.update()
        
        clock.tick(100)
        pygame.display.update(updatesprites)
        updatesprites.clear()

    pygame.quit()

# this calls the 'main' function when this script is executed
if __name__ == '__main__':
    main()

