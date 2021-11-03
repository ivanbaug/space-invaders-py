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
BOTTOM_BOUNDARY = -380


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

    if x_dist <= x_max_dist and y_dist <= y_max_dist:
        return True

    return False


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

additional_msg = ""
game_is_on = True
refresh_speed = 20 / 1000

while game_is_on:

    screen.update()
    # Wait screen
    if not scoreb.start_level:
        screen.onkeypress(key="space", fun=None)
        if scoreb.level > 1:
            info_msg.display(f"{additional_msg}\nPress 'p' to start")
        else:
            info_msg.display(
                f"{additional_msg}\nPress 'p' to start\nTo shoot press 'space'"
            )
        x, y = ship.pos()
        bullet.reload()
        bullet.follow_ship((x, y + B_OFFSET))
        bullet.set_speed(scoreb.level_speed())
    if scoreb.start_level:
        screen.onkeypress(key="space", fun=bullet.fire)
        info_msg.display("")

    # In game
    while scoreb.start_level:
        if bullet.is_fired:
            bullet.move()
            screen.onkeypress(key="space", fun=None)
        else:
            screen.onkeypress(key="space", fun=bullet.fire)
            x, y = ship.pos()
            bullet.follow_ship((x, y + B_OFFSET))

        # Refresh view
        am.displace_aliens()
        screen.update()
        time.sleep(refresh_speed)

        if not am.all_invaders:
            # End game if player passes all levels
            if scoreb.level == 3:
                info_msg.display("🚀🚀 You win! 🚀🚀")
                scoreb.game_win()
                game_is_on = False
                break
            additional_msg = "Level completed!👍"
            refresh_speed *= 0.5
            scoreb.level_completed()

            x, y = ship.pos()
            bullet.follow_ship((x, y + B_OFFSET))
            am.create_aliens()

        # detect collision with wall
        if bullet.ycor() > TOP_BOUNDARY:
            bullet.reload()

        for i, alien in enumerate(am.all_invaders):
            # bullet collision with aliens
            collides = det_collision(alien, bullet)
            if collides:
                bullet.reload()
                am.remove_alien(i)
                scoreb.point_for_plyer()

            # alien collision with ship
            collides = det_collision(alien, ship)
            if collides:
                additional_msg = "You lost a ship"
                scoreb.lost_life()
                am.reset_al_positions()

            # alien lands planet
            if alien.ycor() < BOTTOM_BOUNDARY:
                additional_msg = "Aliens landed your planet\nYou lost a ship"
                scoreb.lost_life()
                am.reset_al_positions()

            if scoreb.lives == 0:
                info_msg.display("👾 Game over 👾")
                scoreb.game_over()
                game_is_on = False
                break


screen.exitonclick()
