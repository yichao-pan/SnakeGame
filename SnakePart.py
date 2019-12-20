from Drawable import Drawable
from Const import Colors
import pygame


class SnakePart(Drawable):

    def __init__(self, pos, grid_size):
        Drawable.__init__(self)
        self.pos = pos
        self.prev_pos = (pos[0], pos[1] - grid_size)

        # self.next = next
        self.size = grid_size

    # def add_part(self):
    #     if(self.is_tail()):
    #         self.next = SnakePart((self.x_pos, self.y_pos), self.size, None)
    #     else:
    #         self.next.add_part()

    # def is_tail(self):
    #     if (self.next == None):
    #         return True
    #     else:
    #         return False

    def move(self, new_pos):
        # if(self.is_tail() == False):
        #     self.next.move((self.x_pos, self.y_pos))
        self.prev_pos = self.pos
        self.pos = new_pos

    def draw(self, screen):
        pygame.draw.rect(screen,
                         Colors.GREEN,
                         (self.pos, (self.size, self.size))
                         )
        # if(self.is_tail() == False):
        #     self.next.draw(screen)
