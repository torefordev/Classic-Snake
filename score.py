import turtle

class Score(turtle.Turtle):

    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.point = 0
        self.setpos(0,280)
        self.update_score()

    def update_score(self):
        self.write(f"Score: {self.point}", move=False, align='center', font=('Comic Sans MS', 12, 'normal'))

    def game_over(self):
        self.setpos(0,0)
        self.clear()
        self.write(f"GAME OVER\nYour score is: {self.point}", move=False, align='center', font=('Comic Sans MS', 30, 'bold'))

    def increase(self):
        self.point += 1
        self.clear()
        self.update_score()