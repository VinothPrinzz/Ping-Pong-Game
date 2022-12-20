from turtle import Turtle


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score1 = 0
        self.score2 = 0
        self.color('white')
        self.penup()
        self.hideturtle()
        self.update_score()

    def update_score(self):
        self.clear()
        self.goto(200, 250)
        self.write(f"Score = {self.score1}",
                   align='center',
                   font=('Arial', 24, 'normal'))

        self.goto(-200, 250)
        self.write(f"Score = {self.score2}",
                   align='center',
                   font=('Arial', 24, 'normal'))

    def increase_score1(self):
        self.score1 += 1
        self.update_score()

    def increase_score2(self):
        self.score2 += 1
        self.update_score()