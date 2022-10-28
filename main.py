from turtle import Turtle, Screen
from paddle import Paddle
from ball import Ball
import time
from scoreboard import Scoreboard

turtle = Turtle()
screen = Screen()
screen.tracer(0)
game_is_on = True

def is_player_on():
    question = input("Type '1' to play a 1-player game. Type '2' to play a 2-player game.").lower()
    if question == "1" or question == "one":
        return True
    else:
        return False

r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))
ball = Ball()
scoreboard = Scoreboard()

screen.bgcolor("deep sky blue")
screen.setup(width=800, height=600)
screen.title("PONGGGG")

# Set paddle controls

screen.listen()

screen.onkeypress(fun=l_paddle.go_up, key="w")
screen.onkeypress(fun=r_paddle.go_up, key="Up")

screen.onkeypress(fun=l_paddle.go_down, key="s")

screen.onkeypress(fun=r_paddle.go_down, key="Down")




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
    
    if is_player_on():
        if l_paddle.ycor() < ball.ycor() and abs(l_paddle.ycor() - ball.ycor()) > 10:
            l_paddle.go_up()
        elif l_paddle.ycor() > ball.ycor() and abs(l_paddle.ycor() - ball.ycor()) > 10:
            l_paddle.go_down()


screen.exitonclick()
