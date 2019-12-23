from Drawable import *


class Item(Drawable):

    def __init__(self, pos, size):
        self.pos = pos
        self.size = size

    def draw(self, screen):
        pygame.draw.circle(screen,
                           Colors.YELLOW,
                           (int(self.pos[0] + self.size / 2), int(self.pos[1] + self.size / 2)),
                           int(self.size / 2)
                           )

    def __str__(self):
        return str(self.pos)
