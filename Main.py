from Item import Item
from Snake import Snake
from Map import *
from random import seed
from random import randint


def add_item():
    valid_pos = False
    item_pos = (0, 0)
    while not valid_pos:
        # seed(42)
        item_x_pos = randint(0, (WIN_WIDTH / GRID_SIZE)-1) * GRID_SIZE
        item_y_pos = randint(0, (WIN_HEIGHT / GRID_SIZE)-1) * GRID_SIZE
        item_pos = [item_x_pos, item_y_pos]
        valid_pos = True

        # check that the item did not spawn on top of a snake
        for s in player.snake_list:
            if (s.pos == item_pos):
                valid_pos = False
    print(item_pos)
    item_list.append(Item(item_pos, GRID_SIZE))


pygame.init()

# set up window
WIN_WIDTH = 500
WIN_HEIGHT = 500
GRID_SIZE = 20
win = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT))

# set up map
game_map = Map([WIN_WIDTH, WIN_HEIGHT], GRID_SIZE)

# set up player
player = Snake([WIN_WIDTH, WIN_HEIGHT], GRID_SIZE, 100, speed=1, starting_length=5)
next_dir = 0

# set up items
MAX_ITEMS = 3
item_list = []
add_item()

# set up clock
clock = pygame.time.Clock()
FPS = 60
GAMESPEED = 0.01
update_counter = 0
spawn_counter = 0
SPAWN_TIME = 10

run = True
while run:

    # check for events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    # movement
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        next_dir = 1
    if keys[pygame.K_RIGHT]:
        next_dir = 3
    if keys[pygame.K_UP]:
        next_dir = 2
    if keys[pygame.K_DOWN]:
        next_dir = 4

    if (player.head_grid_align()):
        player.change_dir(next_dir)
        next_dir = 0

    if (update_counter == 1 / GAMESPEED):
        update_counter = 0
        player.move()
        player.update_facing()
        # check if snake is touching itself
        if (player.check_collision()):
            run = False

        # check if player is over item
        for i in item_list:
            if (player.get_head().pos == i.pos):
                item_list.remove(i)
                player.add_part()
                add_item()

        # if(spawn_counter == SPAWN_TIME * FPS):
        #     spawn_counter = 0
        #     if(len(item_list)<MAX_ITEMS):
        #         add_item()

    # draw
    win.fill((0, 0, 0))
    game_map.draw(win)
    for i in item_list:
        i.draw(win)
    player.draw(win)
    pygame.display.update()

    update_counter += 1
    spawn_counter += 1
    clock.tick(FPS)

pygame.quit()
