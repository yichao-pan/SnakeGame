from Drawable import *
import pygame


class SnakePart(Drawable):

    def __init__(self, pos, grid_size, speed, facing):
        Drawable.__init__(self)
        self.pos = pos
        self.prev_pos = [pos[0], pos[1] - grid_size]

        self.size = grid_size
        self.speed = speed
        self.facing = facing
        self.next_facing = facing

    def move(self, new_pos):
        self.prev_pos = self.pos
        self.pos = new_pos

    def draw(self, screen):
        pygame.draw.rect(screen,
                         Colors.GREEN,
                         (self.pos, (self.size, self.size))
                         )

    def draw_tail(self, screen):
        tail_rec = [
            [self.pos[0], self.pos[1]],
            [self.pos[0] + self.size - 1, self.pos[1]],
            [self.pos[0] + self.size - 1, self.pos[1] + self.size - 1],
            [self.pos[0], self.pos[1] + self.size - 1]
        ]
        # left
        if (self.next_facing == 1):
            tail_rec = [
                [self.pos[0], self.pos[1]],
                [self.pos[0] + self.size - 2, (self.pos[1] + self.size / 2) - 1],
                [self.pos[0] + self.size - 2, self.pos[1] + self.size / 2],
                [self.pos[0], self.pos[1] + self.size - 1]
            ]
        # right
        if (self.next_facing == 3):
            tail_rec = [
                [self.pos[0] + self.size - 1, self.pos[1]],
                [self.pos[0] + 1, (self.pos[1] + self.size / 2) - 1],
                [self.pos[0] + 1, self.pos[1] + self.size / 2],
                [self.pos[0] + self.size - 1, self.pos[1] + self.size - 1]
            ]
        # up
        if (self.next_facing == 2):
            tail_rec = [
                [self.pos[0], self.pos[1]],
                [self.pos[0] + self.size - 1, self.pos[1]],
                [self.pos[0] + self.size / 2, self.pos[1] + self.size - 2],
                [(self.pos[0] + self.size / 2) - 1, self.pos[1] + self.size - 2],
            ]
        # down
        if (self.next_facing == 4):
            tail_rec = [
                [(self.pos[0] + self.size / 2) - 1, self.pos[1] + 1],
                [self.pos[0], self.pos[1] + self.size - 1],
                [self.pos[0] + self.size - 1, self.pos[1] + self.size - 1],
                [self.pos[0] + self.size / 2, self.pos[1] + 1]
            ]

        pygame.draw.polygon(screen,
                            Colors.GREEN,
                            tail_rec
                            )
