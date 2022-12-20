from turtle import Turtle
import random


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape('circle')
        self.color('white')
        self.x_move = 10
        self.y_move = 10
        self.sleep = 0.1

    def move_ball(self):
        self.penup()
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)

    def bounce(self):
        self.y_move *= -1
        self.sleep *= 0.9

    def collusion(self):
        self.x_move *= -1
        # self.move_ball()

    def reset(self):
        self.goto(0, 0)
        self.x_move *= -1
        self.sleep = 0.1
    

