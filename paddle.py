from turtle import Turtle


class Paddle(Turtle):
    def __init__(self, position):
        super().__init__()
        self.setheading(90)
        self.shape("square")
        self.color("white")
        self.shapesize(stretch_wid=1, stretch_len=5)
        self.penup()
        self.goto(position)

    def go_up(self):
        new_coords = (self.xcor(), self.ycor() + 20)
        if self.ycor() >= 240:
            new_coords = (self.xcor(), self.ycor())
        self.goto(new_coords)

    def go_down(self):
        new_coords = (self.xcor(), self.ycor() - 20)
        if self.ycor() <= -240:
            new_coords = (self.xcor(), self.ycor())
        self.goto(new_coords)







