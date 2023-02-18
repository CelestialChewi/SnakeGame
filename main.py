import turtle
from turtle import Turtle, Screen
from snake import Snake
from food import Food
from score import Score
import time
import random

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Welcome to Snake Game")
screen.tracer(0)

# Stuff
snake1 = Snake()
food1 = Food()
score1 = Score()

# Controller
screen.listen()
screen.onkey(snake1.left, "Left")
screen.onkey(snake1.right, "Right")
screen.onkey(snake1.up, "Up")
screen.onkey(snake1.down, "Down")


game_on = True
while game_on:
    screen.update()
    time.sleep(0.1)
    snake1.move()

    # Collision with food
    if snake1.head.distance(food1) < 15:
        print("Eaten")
        food1.respawn_food()
        score1.add_score()
        snake1.extend()

    # Collision with wall
    if snake1.head.xcor() > 295 or snake1.head.xcor() < -295 or snake1.head.ycor() > 300 or snake1.head.ycor() < -290:
        game_on = False

    # Collision with tail
    for segment in snake1.segments:
        if segment != snake1.head:
            if snake1.head.distance(segment) <= 1e-6:
                game_on = False
                print("Game over")



screen.exitonclick()
