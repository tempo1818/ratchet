import pygame
import sys
import time
pygame.init()

DEFAULT_SCREEN_WIDTH = 800
DEFAULT_SCREEN_HEIGHT = 600
fullscreen = False
fullscreenSize = pygame.display.Info()
fullscreenWidth = fullscreenSize.current_w
fullscreenHeight = fullscreenSize.current_h
screen = pygame.display.set_mode((fullscreenWidth, fullscreenHeight ))
pygame.display.set_caption("Rachet")
running = True

while running:
    
time.sleep(5)