from turtle import Turtle, register_shape


DISPLACEMENT = 30

# Paddle size variables
STRETCH_X = 6
STRETCH_Y = 1


class Paddle(Turtle):
    def __init__(self, start_pos, screen_size):
        super().__init__()
        register_shape("project\\img\\ship.gif")
        self.shape("project\\img\\ship.gif")
        # self.shapesize(stretch_len=STRETCH_X, stretch_wid=STRETCH_Y)
        # self.color("white")
        self.speed("fastest")
        self.penup()
        self.goto(start_pos)
        # Left limit = -half of the screen width + half of the paddle width in pixels
        # Paddle width in pixels = stretch * 20px
        self.x_limit_L = -screen_size[0] / 2 + 50
        # Left limit = half of the width - half of the paddle width in pixels - 10 lost pixels from the bezel of the screen :/
        self.x_limit_R = screen_size[0] / 2 - 50
        self.w = STRETCH_X * 20  # px
        self.h = STRETCH_Y * 20  # px

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
        # print(f"left...x:{x}, y:{y}")
        if x > self.x_limit_L:
            self.goto(x - DISPLACEMENT, y)

    def move_right(self):

        x, y = self.pos()
        # print(f"right...x:{x}, y:{y}")
        if x < self.x_limit_R:
            self.goto(x + DISPLACEMENT, y)
