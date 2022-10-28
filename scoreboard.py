from turtle import Turtle, Screen

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.goto(0, 0)

    def make_line(self):
        self.pendown()
        self.backward(10)
        self.penup()

   
