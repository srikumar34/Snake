from turtle import Turtle
from random import random, randint


class Food(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.pu()
        self.resizemode("user")
        self.shapesize(0.4, 0.4, 1)
        self.new_food()

    def new_food(self):
        random_pos = (randint(-280, 280), randint(-280, 280))
        self.setposition(random_pos)
        # self.color(random(), random(), random())
        self.color(0,0,1)

