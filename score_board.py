from turtle import Turtle, Screen


class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        super().hideturtle()
        self.penup()
        self.setposition(0, 270)
        self.color("white")
        self.write(arg="Score:" + str(self.score), move=False, align="center", font=("Times New Roman", 15, "normal"))

    def add(self):
        self.score += 1
        self.clear()
        self.write(arg="Score:" + str(self.score), move=False, align="center", font=("Times New Roman", 15, "normal"))
