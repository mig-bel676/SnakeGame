from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Score
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Miguel's Snake Game")
screen.tracer(0)

game_on = True
slither = Snake()
food = Food()
score = Score()

screen.listen()
screen.onkey(key="Up", fun=slither.up)
screen.onkey(key="Down", fun=slither.down)
screen.onkey(key="Right", fun=slither.right)
screen.onkey(key="Left", fun=slither.left)

food.random_spot()
while game_on:
    screen.update()
    time.sleep(0.08)
    slither.move()
    if slither.head.distance(food) < 15:
        food.random_spot()
        score.update_score()
        slither.extend()
    if slither.head.xcor() > 299 or slither.head.xcor() < -300:
        slither.reset_snake()
        score.reset_score()
    if slither.head.ycor() > 300 or slither.head.ycor() < -299:
        score.reset_score()
        slither.reset_snake()
    for segment in slither.snake[1:]:
        if slither.head.distance(segment) < 10:
            score.reset_score()
            slither.reset_snake()

screen.exitonclick()


