# Importing 'pygame'
import pygame

# Initializing 'pygame'
pygame.init()

# Creating game window of width 400 and height 600
screen = pygame.display.set_mode((400,600))

# Setting the title of the game
pygame.display.set_caption("Rectangles on the same axis")

# Creating RED rectangle
RED=(255,0,0)
red_rect=pygame.Rect(100,200,100,100)
pygame.draw.rect(screen,RED,red_rect)

# Creating GREEN rectangle
GREEN=(0,255,0)
green_rect=pygame.Rect(150,250,100,100)
pygame.draw.rect(screen,GREEN,green_rect)

# Creating BLUE rectangle
BLUE=(0,0,255)
blue_rect=pygame.Rect(200,300,100,100)
pygame.draw.rect(screen,BLUE,blue_rect)

# Updating the screen display
pygame.display.update()
