'''
    Pong Game
    Based on a tutorial from FreeCodeCamp
'''

import turtle

win = turtle.Screen()
win.title('Pong by Antonio')
win.bgcolor('Black')
win.setup(width=800, height=600)
win.tracer(0)

score_a = 0
score_b = 0


def draw_paddle(side, color):
    paddle = turtle.Turtle()
    paddle.speed(0)
    paddle.shape('square')
    paddle.color(color)
    paddle.shapesize(stretch_wid=7, stretch_len=1)
    paddle.penup()
    paddle.goto(side, 0)


def draw_ball(color):
    pass


def left_paddle_up():
    y = left_paddle.ycor()
    y += 20
    left_paddle.sety(y)


def left_paddle_down():
    y = left_paddle.ycor()
    y -= 20
    left_paddle.sety(y)


def right_paddle_up():
    y = right_paddle.ycor()
    y += 20
    right_paddle.sety(y)


def right_paddle_down():
    y = right_paddle.ycor()
    y -= 20
    right_paddle.sety(y)


# Paddle Left
left_paddle = turtle.Turtle()
left_paddle.speed(0)
left_paddle.shape('square')
left_paddle.color('white')
left_paddle.shapesize(stretch_wid=7, stretch_len=1)
left_paddle.penup()
left_paddle.goto(-350, 0)

# Paddle Right
right_paddle = turtle.Turtle()
right_paddle.speed(0)
right_paddle.shape('square')
right_paddle.color('white')
right_paddle.shapesize(stretch_wid=7, stretch_len=1)
right_paddle.penup()
right_paddle.goto(350, 0)

# Draw Ball
ball = turtle.Turtle()
ball.speed(0)
ball.shape('circle')
ball.color('white')
ball.penup()
ball.goto(0, 0)
ball.dx = 2
ball.dy = -2

# Keep score
pen = turtle.Turtle()
pen.speed(0)
pen.color('White')
pen.penup()
pen.hideturtle()
pen.goto(0, 260)

# Main Game

win.listen()
win.onkeypress(left_paddle_up, 'w')
win.onkeypress(left_paddle_down, 's')
win.onkeypress(right_paddle_up, 'Up')
win.onkeypress(right_paddle_down, 'Down')

while True:
    win.update()
    # game_score()

    # Ball movement
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    # Border limit
    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1

    if ball.ycor() < -280:
        ball.sety(-280)
        ball.dy *= -1

    if ball.xcor() > 390:
        ball.goto(0, 0)
        score_a += 1
        print(score_a)
        ball.dx *= -1
        pen.clear()
        pen.write(f"Player A:  {str(score_a)}    Player B: {str(score_b)}", align='center',
                  font=('Courier', 24, 'normal'))

    if ball.xcor() < -390:
        ball.goto(0, 0)
        score_b += 1
        print(score_b)
        ball.dx *= -1
        pen.clear()
        pen.write(f"Player A:  {str(score_a)}    Player B: {str(score_b)}", align='center',
                  font=('Courier', 24, 'normal'))

    # Ball and Paddle collision
    if (340 < ball.xcor() < 350) and (
            right_paddle.ycor() + 60 > ball.ycor() > right_paddle.ycor() - 60):
        ball.setx(340)
        ball.dx *= -1

    if (-340 > ball.xcor() > -350) and (
            left_paddle.ycor() + 60 > ball.ycor() > left_paddle.ycor() - 60):
        ball.setx(-340)
        ball.dx *= -1
