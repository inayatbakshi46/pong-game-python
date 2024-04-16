from turtle import Turtle, Screen
import time
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
score = Scoreboard()
pong = Ball()
l_paddle = Paddle((-350, 0))
r_paddle = Paddle((350, 0))
screen = Screen()
screen.tracer(0)
screen.onkey(l_paddle.up, "w")
screen.onkey(r_paddle.up, "Up")
screen.onkey(l_paddle.down, "s")
screen.onkey(r_paddle.down, "Down")
screen.listen()
screen.setup(800,600)
screen.bgcolor("black")
screen.title("Pong")

game_is_on = True
while game_is_on:
    time.sleep(pong.move_speed)
    screen.update()
    pong.move()
    if pong.ycor() >= 280 or pong.ycor() <= -280:
        pong.bounce_y()
        
    if pong.distance(r_paddle) < 50 and pong.xcor() > 320 or pong.distance(l_paddle) < 50 and pong.xcor() < -320:
        pong.bounce_x()
        
    if pong.xcor() > 380:
        pong.restart()
        score.l_point()
    
    if pong.xcor() < -380:
        pong.restart()
        score.r_point()
    


screen.exitonclick()