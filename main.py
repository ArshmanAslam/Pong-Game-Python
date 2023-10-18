from turtle import Screen
from paddle import Paddle
from ball import Ball
import time
from score import Score

screen = Screen()
screen.setup(800, 600)
screen.bgcolor('black')
screen.tracer(0)
paddle_right = Paddle(350, 0)
paddle_left = Paddle(-350, 0)
ball = Ball()
screen.listen()
screen.onkey(paddle_left.up, 'w')
screen.onkey(paddle_right.up, 'Up')
screen.onkey(paddle_left.down, 's')
screen.onkey(paddle_right.down, 'Down')
s = Score()
while True:
    screen.update()
    time.sleep(ball.speed)
    ball.move()
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.detect()

    if ball.distance(paddle_right) < 40 and ball.xcor() > 320 or ball.distance(paddle_left) < 40 and ball.xcor() < -320:
        ball.detect_paddle()

    if ball.xcor() > 380:
        s.l_score()
        ball.reset()

    if ball.xcor() < -380:
        s.r_score()
        ball.reset()
# If You Find ANy Problems Or Bugs Feel Free To Contact Me On My Linkdin
