from turtle import Screen, Turtle
from paddle import Paddle
from ball import Ball

from scoreboard import Scoreboard, FONT, Message
from alien_manager import AlienManager
import time


def draw_border():
    border = Turtle()
    border.color("white")
    border.speed(0)
    border.pensize(3)
    border.penup()
    border.goto(-300, 350)
    border.pendown()
    border.forward(600)
    border.left(-90)
    border.forward(750)
    border.left(-90)
    border.forward(600)
    border.left(-90)
    border.forward(750)
    border.penup()
    border.hideturtle()


def det_collision(obj1, obj2):

    x_max_dist = (obj1.w + obj2.w) / 2
    x_dist = abs(obj1.xcor() - obj2.xcor())
    y_max_dist = (obj1.h + obj2.h) / 2
    y_dist = abs(obj1.ycor() - obj2.ycor())

    ratio_x = x_dist / x_max_dist
    ratio_y = y_dist / y_max_dist

    if x_dist <= x_max_dist and y_dist <= y_max_dist:
        if ratio_x > ratio_y:
            # Bounce on x axis
            return True, True
        else:
            # Bounce on y axis
            return True, False
    return False, False


# Screen  size
S_WIDTH = 700
S_HEIGHT = 900


# Setting the screen up
screen = Screen()
screen.setup(width=S_WIDTH, height=S_HEIGHT)
screen.bgcolor("black")
screen.title("Ivan's Space Invaders Game")
# BG Source https://unsplash.com/@fabiolik
screen.bgpic("project\\img\\sspace.gif")
screen.listen()
screen.tracer(0)  # update screen on command


# A turtle for information messages
info_msg = Message(origin=(0, -250))
info_msg.display("hi dude")
title = Message(origin=(0, 390), font=("Consolas", 40, "bold"))
title.display("SPACE INVADERS")
# Scoreboard
scoreb = Scoreboard()
# Boundary
draw_border()


# Paddle math for pos x:
# pos x = half the height in negative coordinates +
# half the height of the paddle assuming a total of 20px (default turtle size) +
# float 20 pixels so you can see the ball fall

paddle_pos_x = (-S_HEIGHT / 2) + 10 + 70
pd = Paddle((0, paddle_pos_x), (S_WIDTH, S_HEIGHT))

ball = Ball()


bm = AlienManager((S_WIDTH, S_HEIGHT))
bm.create_bricks()


screen.onkeypress(key="Left", fun=pd.move_left)
screen.onkeypress(key="Right", fun=pd.move_right)
screen.onkeypress(key="space", fun=scoreb.begin_level)

game_is_on = True


while game_is_on:

    screen.update()

    if not scoreb.start_level:
        x, y = pd.pos()
        ball.follow_paddle((x, y + pd.h))
        ball.set_speed(scoreb.level_speed())

    while scoreb.start_level:

        ball.move()
        screen.update()
        time.sleep(ball.move_speed)

        if not bm.all_bricks:
            if scoreb.level == 5:

                scoreb.game_win()
                game_is_on = False
                break

            scoreb.level_completed()
            x, y = pd.pos()
            ball.follow_paddle((x, y + pd.h))
            bm.create_bricks()

        # detect collision with wall

        if ball.ycor() > S_HEIGHT / 2 - 20:
            ball.bounce_y()

        if ball.xcor() > (S_WIDTH / 2 - 16 - 10) or ball.xcor() < -(S_WIDTH / 2 - 16):
            ball.bounce_x()

        # collision with bricks
        for i, brick in enumerate(bm.all_bricks):
            collides, c_x = det_collision(brick, ball)
            if collides:
                if c_x:
                    ball.bounce_x()
                else:
                    ball.bounce_y()
                bm.remove_brick(i)
                scoreb.point_for_plyer()

        #  Paddle Collision detection
        collides, c_x = det_collision(pd, ball)
        if collides:
            if c_x:
                ball.bounce_x()
            else:
                ball.bounce_y()

        # detect lost ball
        if ball.ycor() < -S_HEIGHT / 2:
            scoreb.lost_life()
            if scoreb.lives == 0:
                scoreb.game_over()
                game_is_on = False
                break


screen.exitonclick()
