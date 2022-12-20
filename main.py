from turtle import Turtle, Screen
from time import sleep
from ScakeBoard import Scake
from ball import Ball
from ScoreBoard import Scoreboard

screen = Screen()
screen.bgcolor('black')
screen.setup(800, 600)
screen.tracer(0)
# sleep(2)

tim = Turtle()
tim.speed('slow')
tim.color('white')
tim.penup()
tim.goto(0, 300)
tim.right(90)
tim.pensize(4)


sb1 = Scake([350, 0])
sb2 = Scake([-350, 0])


ball = Ball()


while True:
    tim.pendown()
    tim.forward(10)
    tim.penup()
    tim.forward(10)
    if tim.ycor() < -300:
        break


screen.listen()


screen.onkey(sb1.r_up, 'Up')
screen.onkey(sb1.r_down, 'Down')
screen.onkey(sb2.l_up, 'w')
screen.onkey(sb2.l_down, 's')

score = Scoreboard()

game_on = True
while game_on:
    sleep(ball.sleep)
    screen.update()
    ball.move_ball()
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce()

    if ball.distance(sb1) < 50 and ball.xcor() > 330:
        ball.collusion()
        score.increase_score1()
        # ball.sleep(ball.increase_speed())

    elif ball.distance(sb2) < 50 and ball.xcor() < -330:
        ball.collusion()
        score.increase_score2()
        # ball.sleep(ball.increase_speed())

    if ball.xcor() > 380 or ball.xcor() < -380:
        ball.reset()




screen.exitonclick()
