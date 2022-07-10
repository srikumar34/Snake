from turtle import Turtle
from random import random


class Snake:

    def __init__(self):
        self.turtles = []
        self.create_snake()
        self.head = self.turtles[0]

    def add_segment(self):
        n = -1
        self.turtles.append(Turtle("square"))
        # self.turtles[n].color(random(), random(), random())
        self.turtles[n].color(1,1,1)
        self.turtles[n].penup()
        self.turtles[n].resizemode("user")
        self.turtles[n].shapesize(0.75, 0.75, 0)
        self.turtles[n].speed("fastest")

    def grow(self):
        get_pos = self.turtles[-1].pos()
        # print(get_pos)
        self.add_segment()
        self.turtles[-1].setpos(get_pos)

    def create_snake(self):
        for n in range(3):
            self.add_segment()
            self.turtles[n].setpos(-15 * n, 0)

    def move(self):
        for x in range(len(self.turtles) - 1, 0, -1):
            pos_tuple = self.turtles[x - 1].pos()
            self.turtles[x].goto(pos_tuple)
        self.head.forward(15)

    def up(self):
        if self.turtles[0].heading() != 270:
            self.turtles[0].seth(90)

    def down(self):
        if self.turtles[0].heading() != 90:
            self.turtles[0].seth(270)

    def left(self):
        if self.turtles[0].heading() != 0:
            self.turtles[0].seth(180)

    def right(self):
        if self.turtles[0].heading() != 180:
            self.turtles[0].seth(0)
