from SnakePart import *


class SnakeHead(SnakePart):

    def __init__(self, pos, grid_size, speed):
        SnakePart.__init__(self, pos, grid_size)
        self.speed = speed * grid_size
        self.move_dir = 4

    def move_head(self, bounds):
        # left
        if (self.move_dir == 1):
            self.move(((self.pos[0]-self.speed) % bounds[0], self.pos[1]))
        # right
        if (self.move_dir == 3):
            self.move(((self.pos[0]+self.speed) % bounds[0], self.pos[1]))
        # up
        if (self.move_dir == 2):
            self.move((self.pos[0], (self.pos[1]-self.speed) % bounds[1]))
        # down
        if (self.move_dir == 4):
            self.move((self.pos[0], (self.pos[1]+self.speed) % bounds[1]))

    def draw(self, screen):
        self.draw_tongue(screen)
        SnakePart.draw(self, screen)


    def draw_tongue(self, screen):
        tongue_size = self.size / 2
        tongue_x_pos = (self.pos[0] + self.size / 2) - (tongue_size / 2)
        tongue_y_pos = (self.pos[1] + self.size / 2) - (tongue_size / 2)

        # left
        if (self.move_dir == 1):
            tongue_x_pos = self.pos[0] - tongue_size / 2
        # right
        if (self.move_dir == 3):
            tongue_x_pos = self.pos[0] + self.size / 2 + tongue_size / 2
        # up
        if (self.move_dir == 2):
            tongue_y_pos = self.pos[1] - tongue_size / 2
        # down
        if (self.move_dir == 4):
            tongue_y_pos = self.pos[1] + self.size / 2 + tongue_size / 2

        pygame.draw.rect(screen,
                         Colors.RED,
                         (tongue_x_pos, tongue_y_pos, tongue_size, tongue_size)
                         )