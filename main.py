from turtle import Screen, Turtle
import time
from snake import Snake
from food import Food
from score import Score

screen = Screen()
screen.setup(600,600)
screen.bgcolor("grey")
screen.title("Classic Snake Game")
screen.tracer(0)


leo = Snake()
food = Food()
score = Score()
screen.update()
screen.listen()

screen.onkey(leo.up,"w")
screen.onkey(leo.left,"a")
screen.onkey(leo.down,"s")
screen.onkey(leo.right,"d")


gaming = True
while gaming:
    screen.update()
    time.sleep(.05)
    leo.move()

    if leo.head.distance(food) < 5:
        food.respawn()
        score.increase()
        leo.extend()

    if leo.head.xcor() >= 300 or leo.head.xcor() <= -310 or leo.head.ycor() >= 310 or leo.head.ycor() <= -300:
        gaming = False
        score.game_over()

    for part in leo.snake_parts[1:]:
        if leo.head.distance(part) < 5:
            gaming = False
            score.game_over()















screen.exitonclick()