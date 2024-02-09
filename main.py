from turtle import Turtle, Screen
from paddle import Paddle
from ball import Ball
import time

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong")
screen.tracer(0)

l_paddle = Paddle((-370, 0))
r_paddle = Paddle((360, 0))
ball = Ball()

screen.listen()
screen.onkey(r_paddle.go_up, "Up")
screen.onkey(r_paddle.go_down, "Down")
screen.onkey(l_paddle.go_up, "w")
screen.onkey(l_paddle.go_down, "s")

game_is_on = True 
while game_is_on:
    time.sleep(0.1)
    screen.update()
    ball.move()

    # Detect collision with wall
    if ball.ycor() > 300 or ball.ycor() < -300:
        ball.bounce_y()

    # Detect collision with r_paddle
    if ball.distance(r_paddle) < 50 and ball.xcor() > 320 or ball.distance(l_paddle) < 50 and ball.xor() < -320:
        ball.bounce_x()

    # Detect when right paddle misses
    if ball.xcor() > 380:
        ball.reset_position()

    # Detect when left paddle misses
    if ball.xcor() < -380:
        ball.reset_position()
        




screen.exitonclick()