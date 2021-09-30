# Importing 'pygame'
import pygame

# Initializing 'pygame'
pygame.init()

# Creating game window of width 400 and height 600
screen = pygame.display.set_mode((400,600))

# Setting the title of the game
pygame.display.set_caption("Rectangles on the same axis")

# Creating RED rectangle
RED=(          )
red_rect=pygame.Rect(100,200,100,100)
pygame.draw.rect(screen,RED,red_rect)

# Creating GREEN rectangle
GREEN=(        )
green_rect=pygame.Rect(150,250,100,100)
pygame.draw.rect(screen,GREEN,green_rect)

# Creating BLUE rectangle
BLUE=(         )
# x = (x of green_rect) + (width/2) 
# y = (y of green_rect) + (height/2) 
blue_rect=pygame.Rect(    ,     ,100,100)
pygame.draw.rect(screen,BLUE,blue_rect)

# Updating the screen display
pygame.display.update()
