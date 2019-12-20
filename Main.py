import pygame
from SnakeHead import *
from Const import *

pygame.init()

WIN_WIDTH = 500
WIN_HEIGHT = 500

win = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT))

grid_size = 20

entity_list = []
player = SnakeHead((int(WIN_WIDTH/2), int(WIN_HEIGHT/2)), grid_size, 1)
entity_list.append(player)

clock = pygame.time.Clock()
FPS = 30
snake_len = 0
run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    keys = pygame.key.get_pressed()

    x_move = 0
    y_move = 0
    if keys[pygame.K_LEFT]:
        player.move_dir = 1
    if keys[pygame.K_RIGHT]:
        player.move_dir = 3
    if keys[pygame.K_UP]:
        player.move_dir = 2
    if keys[pygame.K_DOWN]:
        player.move_dir = 4

    player.move()

    if(snake_len<20):
        player.add_part()
        snake_len += 1

    win.fill((0, 0, 0))
    for entity in entity_list:
        entity.draw(win)


    pygame.display.update()

    clock.tick(FPS)

pygame.quit()
