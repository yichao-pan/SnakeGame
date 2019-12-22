from Drawable import *


class Item(Drawable):

    def __init__(self, pos, size):
        self.pos = pos
        self.size = size

    def draw(self, screen):
        pygame.draw.rect(screen,
                         Colors.YELLOW,
                         (self.pos, (self.size, self.size))
                         )