from turtle import Turtle

BULLET_SIZE = 0.8


class Bullet(Turtle):
    def __init__(self):
        super().__init__()
        # self.shape("circle")
        self.shapesize(stretch_len=BULLET_SIZE, stretch_wid=BULLET_SIZE)
        self.penup()
        self.color("orange")
        self.speed("fastest")
        self.x_move = 10
        self.y_move = 10
        self.move_speed = 0.02
        self.is_fired = False
        # Point north
        self.left(90)
        # for collision just a box
        self.w = BULLET_SIZE * 20  # px
        self.h = BULLET_SIZE * 20  # px

    def move(self):
        # new_x = self.xcor() + self.x_move
        # new_y = self.ycor() + self.y_move
        new_x = self.xcor()
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

    def follow_ship(self, coord):
        self.goto(coord)

    def set_speed(self, speed):
        self.move_speed = speed

    def fire(self):
        self.is_fired = True

    def reload(self):
        self.is_fired = False
