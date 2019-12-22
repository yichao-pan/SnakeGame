from SnakeHead import SnakeHead
from SnakePart import SnakePart


class Snake:

    def __init__(self, bounds, grid_size, max_len, starting_length=1):
        head = SnakeHead(
            ((bounds[0] + grid_size) / 2,
             (bounds[1] + grid_size) / 2),
            grid_size, 1)

        self.snake_list = [head]
        self.size = grid_size
        self.bounds = bounds
        self.max_len = max_len
        # add segments if starting length is greater than 1
        if (starting_length > 1):
            for i in range(starting_length - 1):
                self.add_part()

    # get the head of the snake
    def get_head(self):
        return self.snake_list[0]

    # get the tail of the snake (last item in list)
    def get_tail(self):
        return self.snake_list[-1]

    # get the lenght of the snake
    def snake_len(self):
        return len(self.snake_list)

    # add a segment to the snake
    def add_part(self):
        # check if the snake is at its max length
        if (self.snake_len() < self.max_len):
            new_part = SnakePart(self.get_tail().prev_pos, self.size)
            self.snake_list.append(new_part)

    # change direction
    def change_dir(self, direction):
        # the snake can't turn 180 degrees if it has more than one segment
        if (direction - 1 != (self.get_head().move_dir - 1 + 2) % 4 or self.snake_len() <= 1):
            self.get_head().move_dir = direction

    # move the snake
    def move(self):
        # move the head to new position
        self.get_head().move_head(self.bounds)
        # each following segment moves to the old position of the segment before it
        for i in range(1, self.snake_len()):
            self.snake_list[i].move(self.snake_list[i - 1].prev_pos)

    # check if the snake is colliding with itself
    def check_collision(self):
        for i in range(1, self.snake_len()):
            # check if the head's position is overlapping with another segment
            if (self.get_head().pos == self.snake_list[i].pos):
                print("Game Over")
                return True
        return False

    # draw the snake
    def draw(self, screen):
        for s in self.snake_list:
            s.draw(screen)
