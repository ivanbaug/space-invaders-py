from turtle import Turtle, register_shape


DISPLACEMENT = 30

# Width and height in px
SHIP_WIDTH = 46
SHIP_HEIGHT = 42
# Offset for bullet (around half the height)
B_OFFSET = 24


class Ship(Turtle):
    def __init__(self, start_pos, screen_size):
        super().__init__()
        register_shape("project\\img\\ship.gif")
        self.shape("project\\img\\ship.gif")
        self.speed("fastest")
        self.penup()
        self.goto(start_pos)
        # Left limit = -half of the screen width + half of the ship width in pixels
        border_offset = 60
        self.x_limit_L = (-screen_size[0] / 2) + (SHIP_WIDTH / 2) + border_offset
        # Left limit = half of the width - half of the paddle width in pixels - 10 lost pixels from the bezel of the screen :/
        self.x_limit_R = (screen_size[0] / 2) - (SHIP_WIDTH / 2) - border_offset
        # width and height for collision box
        self.w = SHIP_WIDTH  # px
        self.h = SHIP_HEIGHT  # px

    def move_up(self):
        print("up")
        x, y = self.pos()
        self.goto(x, y + DISPLACEMENT)

    def move_down(self):
        print("down")
        x, y = self.pos()
        self.goto(x, y - DISPLACEMENT)

    def move_left(self):
        x, y = self.pos()
        if x > self.x_limit_L:
            self.goto(x - DISPLACEMENT, y)

    def move_right(self):
        x, y = self.pos()
        if x < self.x_limit_R:
            self.goto(x + DISPLACEMENT, y)
