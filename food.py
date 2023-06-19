from turtle import Turtle
from random import randint



class Food(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(0.5,0.5)
        self.color("red")
        self.speed(0)
        self.respawn()

    def respawn(self):
        x = -1
        y = -1
        while x % 20 != 0:
            x = randint(-280, 280)
        while y % 20 != 0:
            y = randint(-280, 280)
        self.setpos(x, y)

