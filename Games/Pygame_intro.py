# __author__ == "Priya"

import pygame, sys
from pygame.locals import *

#Initialize
pygame.init()
#display mode
DISPLAYSURF = pygame.display.set_mode((400,300), 0, 32)
#display caption
pygame.display.set_caption('Drawing')
#Colors
BLACK = (0, 0, 0)
GREY = (128, 128, 128)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
#Fill Display with white
DISPLAYSURF.fill(GREY)
#Drawing different shapes
pygame.draw.polygon(DISPLAYSURF, BLACK, ((20, 130), (10,140), (60, 200), (120, 240), (78, 150)))
pygame.draw.line(DISPLAYSURF, GREEN, (130, 10), (250, 20),15)
pygame.draw.line(DISPLAYSURF, GREEN, (250,20),(180,60),15)
pygame.draw.line(DISPLAYSURF, GREEN, (180, 60), (130, 10),15)
pygame.draw.circle(DISPLAYSURF, BLUE, (300,100), 40, 0)
pygame.draw.rect(DISPLAYSURF, RED, (200,150,100,100))

#Runs until we get quit command
while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    pygame.display.update()