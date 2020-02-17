'''
    Pong Game
    Based on a tutorial from FreeCodeCamp
'''

import turtle

win = turtle.Screen()
win.bgcolor('Black')
win.setup(width=800, height=600)
win.tracer(0)


def draw_paddle(side):
    paddle_left = turtle.Turtle()
    paddle_left.speed(0)
    paddle_left.shape('square')
    paddle_left.color('white')
    paddle_left.shapesize(stretch_wid=7, stretch_len=1)
    paddle_left.penup()
    paddle_left.goto(side, 0)


# Paddle Left
draw_paddle(-350)

# Paddle Right
draw_paddle(350)

# Main Game

while True:
    win.update()
