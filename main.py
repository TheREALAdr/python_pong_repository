from turtle import Turtle, Screen
from paddle import Paddle

screenturtle =  Turtle()
screen = Screen()
screen.tracer(0)


l_paddle = Paddle((-350, 0))
r_paddle = Paddle((350, 0))

game_is_on = True


# player_paddle = Paddle(paddle_type="player")
# ai_paddle = Paddle(paddle_type="ai")


screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("PONGGGG")

# Set paddle controls

screen.listen()

screen.onkeypress(fun=l_paddle.go_down, key="Down")

while game_is_on:
  screen.update()


screen.exitonclick()
