from Drawable import *
import pygame


class SnakePart(Drawable):

    def __init__(self, pos, grid_size, speed, facing):
        Drawable.__init__(self)
        self.pos = pos
        self.prev_pos = (pos[0], pos[1] - grid_size)
        self.speed = speed
        self.facing = facing
        self.next_facing = facing

        self.size = grid_size


    def move(self, new_pos):
        # if(self.is_tail() == False):
        #     self.next.move((self.x_pos, self.y_pos))
        self.prev_pos = self.pos
        self.pos = (new_pos[0], new_pos[1])


    def draw(self, screen):
        pygame.draw.rect(screen,
                         Colors.GREEN,
                         (self.pos, (self.size, self.size))
                         )
        # if(self.is_tail() == False):
        #     self.next.draw(screen)
