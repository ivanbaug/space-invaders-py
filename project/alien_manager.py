from turtle import Turtle, register_shape
from typing import Tuple

ALIENS = [
    "project\\img\\alien2.gif",
    "project\\img\\alien1.gif",
    "project\\img\\alien3.gif",
    "project\\img\\alien3.gif",
]

AL_WIDTH_PX = 40
AL_HEIGHT_PX = 40

SPACING_X = 50
SPACING_Y = 30

BORDER_OFFSET = 100
TITLES_OFFSET = 180

DISPLACEMENT = 20

BOUNDARY_RIGHT = 270
BOUNDARY_LEFT = -270


class Alien(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.color("black")
        self.w = AL_WIDTH_PX
        self.h = AL_HEIGHT_PX


class AlienManager:
    def __init__(self, window_size):
        register_shape("project\\img\\alien1.gif")
        register_shape("project\\img\\alien2.gif")
        register_shape("project\\img\\alien3.gif")
        self.all_invaders = []
        self.window_width = window_size[0]
        self.window_height = window_size[1]
        self.max_invaders_x = int(
            (self.window_width - BORDER_OFFSET) / (AL_WIDTH_PX + SPACING_X)
        )
        self.directions = ["right", "down", "left", "down"]
        self.current_alien = 0
        self.current_direction = 0
        self.change_dir_flag = False
        self.first_alien = (0, 0)

    def create_aliens(self):
        space_left_x = self.window_width - self.max_invaders_x * (
            AL_WIDTH_PX + SPACING_X
        )
        x_start = -self.window_width / 2 + (AL_WIDTH_PX / 2) + (space_left_x / 2) - 20
        # x_start = 30
        spacing_top = self.window_height / 2 - TITLES_OFFSET
        self.first_alien = (x_start, spacing_top)
        for i, alien in enumerate(ALIENS):
            # for j in range(1):
            for j in range(self.max_invaders_x):
                new_brick = Alien()
                new_brick.shape(alien)
                new_brick.penup()
                new_brick.goto(
                    x_start + (AL_WIDTH_PX + SPACING_X) * j,
                    spacing_top - ((AL_HEIGHT_PX + SPACING_Y) * i),
                )
                self.all_invaders.append(new_brick)
        self.total_aliens = len(self.all_invaders)

    def remove_alien(self, index):
        self.all_invaders[index].hideturtle()
        self.all_invaders[index].clear()
        del self.all_invaders[index]

    def displace_aliens(self):

        total_aliens = len(self.all_invaders)
        if self.current_alien < total_aliens:
            x, y = self.all_invaders[self.current_alien].pos()
            # get new position
            nx, ny = self.new_position((x, y), self.directions[self.current_direction])

            if nx >= BOUNDARY_RIGHT:
                # print(nx)
                self.change_dir_flag = True
            elif nx <= BOUNDARY_LEFT:
                self.change_dir_flag = True

            self.all_invaders[self.current_alien].goto(nx, ny)
            self.current_alien += 1
        else:
            self.current_alien = 0
            if self.current_direction == 1 or self.current_direction == 3:
                self.new_direction()
                self.change_dir_flag = False
            elif self.change_dir_flag:
                self.new_direction()
                self.change_dir_flag = False

    def new_position(self, current_pos: Tuple, direction: str):
        x, y = current_pos
        new_pos = (x, y)
        if direction == "up":
            new_pos = (x, y + DISPLACEMENT)
        elif direction == "down":
            new_pos = (x, y - DISPLACEMENT)
        elif direction == "right":
            new_pos = (x + DISPLACEMENT, y)
        elif direction == "left":
            new_pos = (x - DISPLACEMENT, y)
        return new_pos

    def new_direction(self):
        if self.current_direction == 3:
            self.current_direction = 0
        else:
            self.current_direction += 1

    def reset_al_positions(self):
        ox, oy = self.first_alien
        cy = self.all_invaders[0].ycor()
        dist_y = oy - cy
        for alien in self.all_invaders:
            alien.sety(alien.ycor() + dist_y)

    # def move_cars(self):
    #     for car in self.all_cars:
    #         car.backward(self.car_speed)

    # def level_up(self):
    #     self.car_speed += MOVE_INCREMENT
