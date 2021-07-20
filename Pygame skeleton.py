import os, sys, time
import pygame
from pygame.locals import *

pygame.init()
mainClock = pygame.time.Clock()

WINDOWWIDTH = 500
WINDOWHEIGHT = 500
windowSurface = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT), 0, 32)
pygame.display.set_caption("pygame")

BLACK = (0, 0, 0)
RED = (255, 0, 0)
WHITE = (255, 255, 255)

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    
    windowSurface.fill(WHITE)
# this is where the screen display changes go

    pygame.display.update()
    time.sleep(0.02)