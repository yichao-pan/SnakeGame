from SnakePart import *


class SnakeHead(SnakePart):

    def __init__(self, pos, grid_size, speed):
        SnakePart.__init__(self, pos, grid_size, None)
        self.speed = speed * grid_size
        self.move_dir = 4

    def move(self):
        SnakePart.move(self,(self.x_pos, self.y_pos))
        # left
        if (self.move_dir == 1):
            self.x_pos -= self.speed
        # right
        if (self.move_dir == 3):
            self.x_pos += self.speed
        # up
        if (self.move_dir == 2):
            self.y_pos -= self.speed
        # down
        if (self.move_dir == 4):
            self.y_pos += self.speed

    def draw(self, screen):
        self.draw_tongue(screen)
        SnakePart.draw(self, screen)


    def draw_tongue(self, screen):
        tongue_size = self.size / 2
        tongue_x_pos = (self.x_pos + self.size / 2) - (tongue_size / 2)
        tongue_y_pos = (self.y_pos + self.size / 2) - (tongue_size / 2)

        # left
        if (self.move_dir == 1):
            tongue_x_pos = self.x_pos - tongue_size / 2
        # right
        if (self.move_dir == 3):
            tongue_x_pos = self.x_pos + self.size / 2 + tongue_size / 2
        # up
        if (self.move_dir == 2):
            tongue_y_pos = self.y_pos - tongue_size / 2
        # down
        if (self.move_dir == 4):
            tongue_y_pos = self.y_pos + self.size / 2 + tongue_size / 2

        pygame.draw.rect(screen,
                         Colors.RED,
                         (tongue_x_pos, tongue_y_pos, tongue_size, tongue_size)
                         )