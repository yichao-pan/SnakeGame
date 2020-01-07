from SnakePart import *


class SnakeHead(SnakePart):

    def __init__(self, pos, speed, grid_size):
        facing = 4
        SnakePart.__init__(self, pos, grid_size, speed, facing)

    def move(self, bounds):
        self.prev_pos = self.pos
        # left
        if (self.facing == 1):
            self.pos = [(self.pos[0]-self.speed * self.size) % bounds[0], self.pos[1]]
        # right
        if (self.facing == 3):
            self.pos = [(self.pos[0]+self.speed * self.size) % bounds[0], self.pos[1]]
        # up
        if (self.facing == 2):
            self.pos = [self.pos[0], (self.pos[1]-self.speed * self.size) % bounds[1]]
        # down
        if (self.facing == 4):
            self.pos = [self.pos[0], (self.pos[1]+self.speed * self.size) % bounds[1]]

    def draw(self, screen):
        self.draw_tongue(screen)
        SnakePart.draw(self, screen)


    def draw_tongue(self, screen):
        tongue_size = self.size / 2
        tongue_x_pos = (self.pos[0] + self.size / 2) - (tongue_size / 2)
        tongue_y_pos = (self.pos[1] + self.size / 2) - (tongue_size / 2)

        # left
        if (self.facing == 1):
            tongue_x_pos = self.pos[0] - tongue_size / 2
        # right
        if (self.facing == 3):
            tongue_x_pos = self.pos[0] + self.size / 2 + tongue_size / 2
        # up
        if (self.facing == 2):
            tongue_y_pos = self.pos[1] - tongue_size / 2
        # down
        if (self.facing == 4):
            tongue_y_pos = self.pos[1] + self.size / 2 + tongue_size / 2

        pygame.draw.rect(screen,
                         Colors.RED,
                         (tongue_x_pos, tongue_y_pos, tongue_size, tongue_size)
                         )