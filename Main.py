from Snake import Snake
from SnakeHead import *
from Const import *
from Map import *


def update():
    player.move()
    player.add_part()

pygame.init()

WIN_WIDTH = 500
WIN_HEIGHT = 500

win = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT))

grid_size = 20
game_map = Map((WIN_WIDTH, WIN_HEIGHT), grid_size)

entity_list = []
player = Snake(SnakeHead(((WIN_WIDTH + grid_size) / 2, (WIN_HEIGHT + grid_size) / 2),
                         grid_size, 1),
               (WIN_WIDTH, WIN_HEIGHT))

entity_list.append(player)

clock = pygame.time.Clock()
FPS = 60
GAMESPEED = 0.1
update_counter = 0

run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    keys = pygame.key.get_pressed()

    x_move = 0
    y_move = 0
    if keys[pygame.K_LEFT]:
        player.change_dir(1)
    if keys[pygame.K_RIGHT]:
        player.change_dir(3)
    if keys[pygame.K_UP]:
        player.change_dir(2)
    if keys[pygame.K_DOWN]:
        player.change_dir(4)

    if (update_counter == 1 / GAMESPEED):
        update()
        update_counter = 0

    win.fill((0, 0, 0))
    game_map.draw(win)
    for entity in entity_list:
        entity.draw(win)

    pygame.display.update()
    update_counter += 1

    clock.tick(FPS)

pygame.quit()
