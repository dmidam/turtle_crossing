from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 5

class CarManager(Turtle):

    def __init__(self, speed):
        super().__init__()
        self.penup()
        self.shape("square")
        self.color(self.car_color())
        self.shapesize(stretch_wid=1, stretch_len=2)
        self.car_generate()
        self.car_color()
        self.speed = speed



    def car_generate(self):
        new_x = 290
        new_y = random.randint(-250, 250)
        self.goto(new_x, new_y)

    def car_move(self):
        self.backward(self.speed)

    def car_color(self):
        color = random.choice(COLORS)
        return color

