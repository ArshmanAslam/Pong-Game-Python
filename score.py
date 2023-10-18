from turtle import Turtle


class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.left_score = 0
        self.right_score = 0
        self.board_maker()

    def board_maker(self):
        self.clear()
        self.color('white')
        self.penup()
        self.hideturtle()
        self.goto(100, 235)
        self.write(self.right_score, align='center', font=('Arial', 50, 'normal'))
        self.goto(-100, 235)
        self.write(self.left_score, align='center', font=('Arial', 50, 'normal'))

    def r_score(self):
        self.right_score += 1
        self.board_maker()

    def l_score(self):
        self.left_score += 1
        self.board_maker()

# If You Find ANy Problems Or Bugs Feel Free To Contact Me On My Linkdin
