from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Courier", 80, "normal")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.color("white")
        self.l_score = 0
        self.r_score = 0
        self.make_line()
        self.update_score()

    def update_score(self):
        self.goto(-100, 200)
        self.write(self.l_score, align=ALIGNMENT, font=FONT)
        self.goto(100, 200)
        self.write(self.r_score, align=ALIGNMENT, font=FONT)

    def l_point(self):
        self.l_score += 1
        self.clear()
        self.update_score()

    def r_point(self):
        self.r_score += 1
        self.clear()
        self.update_score()
        
    def make_line(self):
        self.goto(0, 300)
        while self.ycor() > -300:
            self.pendown()
            self.backward(10)
            self.penup()
