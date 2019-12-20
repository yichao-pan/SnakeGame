import pygame


class Map:
    def __init__(self, bounds, grid_size):
        self.bounds = bounds
        self.grid_size = grid_size

    def draw(self, screen):
        for y in range(0, self.bounds[1], self.grid_size):
            for x in range(0, self.bounds[0], self.grid_size):
                if ((x + y) % (self.grid_size * 2) == 0):
                    pygame.draw.rect(screen,
                                     (25, 25, 25),
                                     ((x, y), (self.grid_size, self.grid_size))
                                     )
