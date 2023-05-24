from game_config import COLS, ROWS

#Defining the snake class
class Snake:
    def __init__(self, start_pos):
        #Initialize the snake with a starting position and not moving
        self.body = [start_pos]
        self.direction = (1, 0)

    def move(self):
        #If the snake has a direction, calculate the new head pos and update its body
        if self.direction != (0, 0):
            new_head = ((self.body[0][0] + self.direction[0]) % COLS, (self.body[0][1] + self.direction[1]) % ROWS)
            self.body.insert(0, new_head)
            self.body.pop()

    def change_direction(self, new_direction):
        self.direction = new_direction

    def get_head(self):
        #Return the head of the snake
        return self.body[0]

    def get_body(self):
        #Return the snakes entire body (without the head)
        return self.body

    def grow(self):
        #Make the snake grow by adding another segnem at the and of its body.
        tail = self.body[-1]
        self.body.append(tail)

    def reset(self, start_pos):
        #Reset the snake to starting position.
        self.body = [start_pos]
        self.direction = (1, 0)

