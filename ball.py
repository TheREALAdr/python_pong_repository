from turtle import Turtle


class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.home()
        self.penup()
        self.x_direct = 10
        self.y_direct = 10
        self.speed = 0.1

    def move(self):
        new_x = self.xcor() + self.x_direct
        new_y = self.ycor() + self.y_direct
        self.goto(new_x, new_y)

    def bounce_y(self):
        self.y_direct *= -1

    def bounce_x(self):
        self.x_direct *= -1
        self.speed *= 0.95

    def reset_position(self):
        self.home()
        self.bounce_x()
        self.speed = 0.1
