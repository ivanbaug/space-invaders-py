from turtle import Screen, Turtle
from vessels import Ship, SHIP_WIDTH, SHIP_HEIGHT, B_OFFSET
from bullet import Bullet

from scoreboard import Scoreboard, FONT, Message
from alien_manager import AlienManager
import time

# Screen  size
SCREEN_WIDTH = 700
SCREEN_HEIGHT = 900
TOP_BOUNDARY = 340


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


# Setting the screen up
screen = Screen()
screen.setup(width=SCREEN_WIDTH, height=SCREEN_HEIGHT)
screen.bgcolor("black")
screen.title("Ivan's Space Invaders Game")
# BG Source https://unsplash.com/@fabiolik
screen.bgpic("project\\img\\sspace.gif")
screen.listen()
screen.tracer(0)  # update screen on command


# A turtle for information messages
info_msg = Message(origin=(0, -250))
info_msg.display("")
title = Message(origin=(0, 390), font=("Consolas", 40, "bold"))
title.display("SPACE INVADERS")
# Scoreboard
scoreb = Scoreboard()

# Boundary
draw_border()


# Position of the ship math for pos x:
# pos x = half the height in negative coordinates +
# half the height of the ship assuming a total of 20px (default turtle size) +
# float 50 pixels
border_offset = 60
ship_pos_x = (-SCREEN_HEIGHT / 2) + SHIP_HEIGHT / 2 + border_offset
ship = Ship((0, ship_pos_x), (SCREEN_WIDTH, SCREEN_HEIGHT))

bullet = Bullet()


am = AlienManager((SCREEN_WIDTH, SCREEN_HEIGHT))
am.create_aliens()


screen.onkeypress(key="Left", fun=ship.move_left)
screen.onkeypress(key="Right", fun=ship.move_right)
screen.onkeypress(key="p", fun=scoreb.begin_level)
screen.onkeypress(key="space", fun=None)

game_is_on = True


while game_is_on:

    screen.update()

    if not scoreb.start_level:
        bullet.reload()
        screen.onkeypress(key="space", fun=None)
        info_msg.display("Press 'p' to start")
        x, y = ship.pos()
        bullet.follow_ship((x, y + B_OFFSET))
        bullet.set_speed(scoreb.level_speed())
    if scoreb.start_level:
        screen.onkeypress(key="space", fun=bullet.fire)
        info_msg.display("")

    while scoreb.start_level:
        if bullet.is_fired:
            bullet.move()
        else:
            x, y = ship.pos()
            bullet.follow_ship((x, y + B_OFFSET))
        screen.update()
        time.sleep(bullet.move_speed)

        if not am.all_invaders:
            if scoreb.level == 5:

                scoreb.game_win()
                game_is_on = False
                break

            scoreb.level_completed()
            x, y = ship.pos()
            bullet.follow_ship((x, y + B_OFFSET))
            am.create_aliens()

        # detect collision with wall

        if bullet.ycor() > TOP_BOUNDARY:
            bullet.reload()

        if bullet.xcor() > (SCREEN_WIDTH / 2 - 16 - 10) or bullet.xcor() < -(
            SCREEN_WIDTH / 2 - 16
        ):
            bullet.bounce_x()

        # collision with bricks
        for i, brick in enumerate(am.all_invaders):
            collides, c_x = det_collision(brick, bullet)
            if collides:
                if c_x:
                    bullet.bounce_x()
                else:

                    bullet.reload()
                am.remove_alien(i)
                scoreb.point_for_plyer()

        #  Paddle Collision detection
        # collides, c_x = det_collision(ship, bullet)
        # if collides:
        #     if c_x:
        #         bullet.bounce_x()
        #     else:
        #         bullet.bounce_y()

        # detect lost ball
        if bullet.ycor() < -SCREEN_HEIGHT / 2:
            scoreb.lost_life()
            if scoreb.lives == 0:
                scoreb.game_over()
                game_is_on = False
                break


screen.exitonclick()
