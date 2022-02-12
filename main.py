# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.
import time
from turtle import Turtle,Screen
from snake import Snake
from food import Food
from score import Scorecard
game_on=True
screen=Screen()
screen.setup(600,600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)
snake=Snake()
food=Food()
scorecard=Scorecard()
screen.listen()
screen.onkey(snake.up,"Up")
screen.onkey(snake.down,"Down")
screen.onkey(snake.left,"Left")
screen.onkey(snake.right,"Right")
while game_on:
    screen.update()
    snake.move()
    time.sleep(0.08)
    if snake.head.distance(food)<17:
        food.refresh()
        snake.extend()
        scorecard.score_update()
    if snake.head.xcor()>295 or snake.head.xcor()<-295 or snake.head.ycor()>295 or snake.head.ycor()<-295:
        scorecard.game_over()
        game_on=False
    for segment in snake.segments:
        if segment==snake.head:
            pass
        elif snake.head.distance(segment)<10:
            scorecard.game_over()
            game_on=False
screen.exitonclick()
