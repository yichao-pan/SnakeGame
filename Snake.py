from SnakeHead import SnakeHead
from SnakePart import SnakePart


class Snake:

    def __init__(self, bounds, grid_size, starting_length = 1):
        head = SnakeHead(
            ((bounds[0] + grid_size) / 2,
             (bounds[1] + grid_size) / 2),
                         grid_size, 1)

        self.snake_list = [head]
        self.size = grid_size
        self.bounds = bounds
        self.max_len = 10
        if(starting_length>1):
            for i in range(starting_length-1):
                self.add_part()

    def get_head(self):
        return self.snake_list[0]

    def get_tail(self):
        print(self.snake_list[-1].pos)
        return self.snake_list[-1]

    def snake_len(self):
        return len(self.snake_list)

    def add_part(self):
        if (self.snake_len() < self.max_len):
            new_part = SnakePart((self.get_tail().prev_pos), self.size)
            self.snake_list.append(new_part)

    def change_dir(self, direction):
        if(direction-1 != (self.get_head().move_dir -1 + 2)%4 or self.snake_len()<=1):
            self.get_head().move_dir = direction

    def move(self):
        self.get_head().move_head(self.bounds)
        for i in range(1, self.snake_len()):
            self.snake_list[i].move(self.snake_list[i - 1].prev_pos)

    def check_collision(self):
        for i in range(1, self.snake_len()):
            if(self.get_head().pos == self.snake_list[i].pos):
                print("collision")
                return True
        return False

    def draw(self, screen):
        for s in self.snake_list:
            s.draw(screen)
