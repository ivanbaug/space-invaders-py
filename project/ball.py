from turtle import Turtle

BALL_DIA = 0.8


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.shapesize(stretch_len=BALL_DIA, stretch_wid=BALL_DIA)
        self.penup()
        self.color("orange")
        self.speed("fastest")
        self.x_move = 10
        self.y_move = 10
        self.move_speed = 0.05
        # for collision just a box
        self.w = BALL_DIA * 20  # px
        self.h = BALL_DIA * 20  # px

    def move(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)

    def bounce_y(self):
        self.y_move *= -1

    def bounce_x(self):
        self.x_move *= -1
        # Speed increase
        # self.move_speed *= 0.5

    def reset_position(self):
        # self.move_speed = 0.1
        self.goto(0, 0)
        # self.bounce_x()

    def follow_paddle(self, coord):
        self.goto(coord)

    def set_speed(self, speed):
        self.move_speed = speed
