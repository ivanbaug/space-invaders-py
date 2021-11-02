from turtle import Turtle, register_shape

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

    def create_aliens(self):
        space_left_x = self.window_width - self.max_invaders_x * (
            AL_WIDTH_PX + SPACING_X
        )
        x_start = -self.window_width / 2 + (AL_WIDTH_PX / 2) + (space_left_x / 2)
        # x_start = 30
        spacing_top = self.window_height / 2 - TITLES_OFFSET
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

    def remove_alien(self, index):
        self.all_invaders[index].hideturtle()
        self.all_invaders[index].clear()
        del self.all_invaders[index]

    # def move_cars(self):
    #     for car in self.all_cars:
    #         car.backward(self.car_speed)

    # def level_up(self):
    #     self.car_speed += MOVE_INCREMENT
