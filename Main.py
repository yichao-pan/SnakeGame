import pygame
from Const import *

pygame.init()

WIN_WIDTH = 500
WIN_HEIGHT = 500

win = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT))

x = 50
y = 50
width = 50
height = 50
vel = 5

clock = pygame.time.Clock()
FPS = 60

run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT]:
        x = x - vel
    if keys[pygame.K_RIGHT]:
        x = x + vel
    if keys[pygame.K_UP]:
        y = y - vel
    if keys[pygame.K_DOWN]:
        y = y + vel
    win.fill((0, 0, 0))

    pygame.draw.rect(win, Colors.GREEN, (x, y, width, height))
    pygame.display.update()

    clock.tick(FPS)
    
pygame.quit()
