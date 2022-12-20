from turtle import Turtle


class Scake(Turtle):
    def __init__(self, position):
        self.all_scake = []
        super().__init__()

        self.shape('square')
        self.shapesize(5, 1)
        self.color('white')
        self.penup()
        self.goto(position)

    def r_up(self):
        new_y = self.ycor() + 20
        self.goto(350, new_y)

    def r_down(self):
        new_y = self.ycor() - 20
        self.goto(350, new_y)

    def l_up(self):
        new_y = self.ycor() + 20
        self.goto(-350, new_y)

    def l_down(self):
        new_y = self.ycor() - 20
        self.goto(-350, new_y)
