from turtle import Screen
from time import sleep
from snake import Snake
from food import Food
from score_board import ScoreBoard
screen = Screen()
screen.setup(height=600, width=600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.listen()
screen.tracer(0)
my_snake = Snake()
score = ScoreBoard()
food = Food()
screen.update()

screen.onkey(my_snake.up, "Up")
screen.onkey(my_snake.down, "Down")
screen.onkey(my_snake.left, "Left")
screen.onkey(my_snake.right, "Right")

is_on = True
while is_on:
    screen.update()
    sleep(0.1)
    my_snake.move()
    if my_snake.head.distance(food) < 15:
        """Snake hits food"""
        my_snake.grow()
        # my_snake.turtles[-1].color(food.fillcolor())
        food.new_food()
        score.add()

    for x in range(2, len(my_snake.turtles)):
        """For snake hitting itself"""
        if my_snake.head.distance(my_snake.turtles[x]) < 15:
            is_on = False
            score.goto(0, 150)
            score.write(arg="Game Over", align="center", font=("Calibre", 20, "normal"))
            screen.update()
            break
    head_pos = my_snake.head.position()
    for z in range(2):
        """For snake hitting wall"""
        if head_pos[z] > 290 or head_pos[z] < -295:
            is_on = False
            score.goto(0, 150)
            score.write(arg="Game Over", align="center", font=("Calibre", 20, "normal"))
            break
screen.exitonclick()
