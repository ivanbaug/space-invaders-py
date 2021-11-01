import turtle
from turtle import Screen

# Screen  size
S_WIDTH = 700
S_HEIGHT = 900
# Setting the screen up
screen = Screen()
screen.setup(width=S_WIDTH, height=S_HEIGHT)
screen.bgcolor("white")
screen.title("Ivan's Space Invaders Game")
# BG Source https://unsplash.com/@fabiolik
screen.bgpic("project\\img\\sspace.gif")
screen.listen()
screen.tracer(0)  # update screen on command
# turtle object
# dimond_turtle = turtle.Turtle()

# # the coordinates
# # of each corner
# shape = ((0, 0), (10, 10), (20, 0), (10, -10))

# # registering the new shape
# turtle.register_shape("diamond", shape)

# # changing the shape to 'diamond'
# dimond_turtle.shape("diamond")

# turtle object
img_turtle = turtle.Turtle()

# registering the image
# as a new shape
turtle.register_shape("project\\img\\ship.gif")

# setting the image as cursor
img_turtle.shape("project\\img\\ship.gif")
img_turtle.penup()

img_turtle.goto(0, -300)

screen.update()
screen.exitonclick()
