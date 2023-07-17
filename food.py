from snake import Snake
from turtle import Turtle
import random


class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shapesize(0.5, 0.5, 1)
        self.penup()
        self.shape("circle")
        self.color("red")

    def random_spot(self):
        r_x = random.randint(-280, 280)
        r_y = random.randint(-280, 280)
        self.goto(x=r_x, y=r_y)

