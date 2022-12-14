from turtle import Turtle, Screen
from paddle import Paddle
from ball import Ball
import time
from scoreboard import Scoreboard

turtle = Turtle()
screen = Screen()
screen.tracer(0)
game_is_on = True

r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))
ball = Ball()
scoreboard = Scoreboard()


def is_1_player():
    response = screen.textinput(title="Gamemode!",
                                prompt="Type '1' for 1-player mode; type '2' for 2-player mode.").lower()
    if response == "1" or response == "one":
        return True
    else:
        return False


def start_ai():
    if l_paddle.ycor() < ball.ycor() and abs(l_paddle.ycor() - ball.ycor()) > 10:
        l_paddle.go_up()
    elif l_paddle.ycor() > ball.ycor() and abs(l_paddle.ycor() - ball.ycor()) > 10:
        l_paddle.go_down()


result = is_1_player()

screen.bgcolor("navy blue")
screen.setup(width=800, height=600)
screen.title("PONGGGG")

# Set paddle controls

screen.listen()

screen.onkeypress(fun=l_paddle.go_up, key="w")
screen.onkeypress(fun=l_paddle.go_down, key="s")

screen.onkeypress(fun=r_paddle.go_up, key="Up")
screen.onkeypress(fun=r_paddle.go_down, key="Down")

screenturtle = Turtle()
screenturtle.color("white")
screenturtle.hideturtle()
screenturtle.pencolor("white")
screenturtle.penup()
screenturtle.goto(0, 300)
screenturtle.setheading(270)
while screenturtle.ycor() != -300:
    screenturtle.pendown()
    screenturtle.forward(15)
    screenturtle.penup()
screenturtle.hideturtle()

while game_is_on:
    time.sleep(ball.speed)
    screen.update()
    ball.move()
    if ball.ycor() >= 280 or ball.ycor() <= -280:
        ball.bounce_y()

    if ball.distance(r_paddle) < 50 and ball.xcor() > 320 or ball.distance(l_paddle) < 50 and ball.xcor() < -320:
        ball.bounce_x()

    if ball.xcor() > 380:
        ball.reset_position()
        scoreboard.l_point()
    if ball.xcor() < -380:
        ball.reset_position()
        scoreboard.r_point()

    # AI Player
    if not result:
        continue
    else:
        start_ai()

screen.exitonclick()
