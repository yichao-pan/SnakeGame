from Drawable import Drawable
from Const import Colors
import pygame


class SnakePart(Drawable):

    def __init__(self, pos, grid_size, next):
        Drawable.__init__(self)
        self.x_pos = pos[0]
        self.y_pos = pos[1]
        self.next = next
        self.size = grid_size

    def add_part(self):
        if(self.is_tail()):
            self.next = SnakePart((self.x_pos, self.y_pos), self.size, None)
        else:
            self.next.add_part()

    def is_tail(self):
        if (self.next == None):
            return True
        else:
            return False

    def move(self, new_pos):
        if(self.is_tail() == False):
            self.next.move((self.x_pos, self.y_pos))
        self.x_pos = new_pos[0]
        self.y_pos = new_pos[1]


    def draw(self, screen):
        pygame.draw.rect(screen,
                         Colors.GREEN,
                         (self.x_pos, self.y_pos, self.size, self.size)
                         )
        if(self.is_tail() == False):
            self.next.draw(screen)
