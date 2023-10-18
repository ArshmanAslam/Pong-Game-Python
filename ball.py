from turtle import Turtle


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape('circle')
        self.color('red')
        self.penup()
        self.y = 10
        self.x = 10
        self.speed = 0.1

    def move(self):
        y = self.ycor() + self.y
        x = self.xcor() + self.x
        self.goto(x, y)

    def detect(self):
        self.y *= -1

    def detect_paddle(self):
        self.x *= -1
        self.speed *= 0.9

    def reset(self):
        self.goto(0, 0)
        self.speed = 0.1
        self.detect_paddle()
# If You Find ANy Problems Or Bugs Feel Free To Contact Me On My Linkdin
