from turtle import Turtle
MOVE_DISTANCE = 20


class Snake:


    def __init__(self):
        self.snake_parts = []
        self.create_snake()
        self.head = self.snake_parts[0]


    def create_snake(self):
        xcor, ycor = 0, 0
        for i in range(3):
            self.add_part(xcor,ycor,"blue")
            xcor -= 20


    def add_part(self,xcor,ycor,color):
        leo = Turtle("square")
        leo.color(color)
        leo.penup()
        leo.setpos(xcor, ycor)
        self.snake_parts.append(leo)

    def extend(self):
        if len(self.snake_parts) % 2 == 0:
            self.add_part(self.snake_parts[-1].xcor(),self.snake_parts[-1].ycor(),"blue")
        else:
            self.add_part(self.snake_parts[-1].xcor(), self.snake_parts[-1].ycor(), "green")


    def move(self):
        for i in range(len(self.snake_parts) - 1, 0, -1):
            self.snake_parts[i].setpos(self.snake_parts[i - 1].pos())
        self.head.forward(MOVE_DISTANCE)

    def up(self):
        if self.head.heading() != 270:
            self.head.setheading(90)
    def left(self):
        if self.head.heading() != 0:
            self.head.setheading(180)
    def down(self):
        if self.head.heading() != 90:
            self.head.setheading(270)
    def right(self):
        if self.head.heading() != 180:
            self.head.setheading(0)

