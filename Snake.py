from SnakePart import SnakePart


class Snake:

    def __init__(self, head, bounds):
        self.snake_list = [head]
        self.size = head.size
        self.bounds = bounds
        self.max_len = 20


    def get_head(self):
        return self.snake_list[0]

    def get_tail(self):
        return self.snake_list[-1]

    def snake_len(self):
        return len(self.snake_list)

    def add_part(self):
        if(self.snake_len()<=self.max_len):
            new_part = SnakePart((self.get_tail().prev_pos), self.size)
            self.snake_list.append(new_part)

    def change_dir(self, direction):
        self.get_head().move_dir = direction

    def move(self):
        self.get_head().move_head(self.bounds)
        for i in range(1, self.snake_len()):
            self.snake_list[i].move(self.snake_list[i-1].prev_pos)

    def draw(self, screen):
        for s in self.snake_list:
            s.draw(screen)
