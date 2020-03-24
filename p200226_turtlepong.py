"""
2020-02-26
game of pong built with the turtle module
based on this tutorial with some minor changes:
https://www.youtube.com/watch?v=XGf2GcyHPhc 

"""

import turtle
import time
import random

global game_on, new_ball
game_on = True
new_ball = True
point = False
score_a = 0
score_b = 0

pad_a_line = -350
pad_b_line = 350
pad_rate = 10

ball_size = 20
ball_dx = 5
ball_dy = 5

wn_width = 800
wn_hight = 600
xmin = 0 - (wn_width / 2) + ball_size
xmax = 0 + (wn_width / 2) - ball_size
ymin = 0 - (wn_hight / 2) + ball_size
ymax = 0 + (wn_hight / 2) - ball_size

# create the game window
wn = turtle.Screen()
wn.title("turtle pong")
wn.bgcolor("black")
wn.setup(width=wn_width, height=wn_hight)
wn.tracer(0)

# create paddle a
pad_a = turtle.Turtle()
pad_a.speed(0)
pad_a.shape("square")
pad_a.color("white")
pad_a.shapesize(stretch_wid=5, stretch_len=1)
pad_a.penup()
pad_a.goto(pad_a_line, 0)

# create paddle b
pad_b = turtle.Turtle()
pad_b.speed(0)
pad_b.shape("square")
pad_b.color("white")
pad_b.shapesize(stretch_wid=5, stretch_len=1)
pad_b.penup()
pad_b.goto(pad_b_line, 0)

# create the ball
ball = turtle.Turtle()
ball.speed(0)
ball.shape("square")
ball.color("white")
ball.penup()
ball.goto(0, 0)

# create the score writing object
pen = turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, wn_hight / 2 - 40)

def update_score(a, b):
    pen.clear()
    pen.write("P1: {}       P2: {}".format(a, b), \
              align="center", font=("Consolas", 24, "bold"))

def quitgame():
    global game_on
    game_on = False

def reset_ball():
    global new_ball
    new_ball = True

def pads_up():
    pad_a.sety(pad_a.ycor() + pad_rate)
    pad_b.sety(pad_b.ycor() + pad_rate)

def pads_dn():
    pad_a.sety(pad_a.ycor() - pad_rate)
    pad_b.sety(pad_b.ycor() - pad_rate)

# key binds
wn.listen()
wn.onkeypress(quitgame, "q")
wn.onkeypress(reset_ball, "r")
wn.onkeypress(pads_up, "w")
wn.onkeypress(pads_dn, "s")

# game main loop
while game_on == True:
    frame_start = time.time()
    wn.update()
    # loop start --------------------
    
    if point:
        point = False
        ball_dx *= -1
        time.sleep(2)
        new_ball = True

    if new_ball:
        new_ball = False
        ball.goto(0, 0)
        ball_dy = 0
        while ball_dy == 0:
            ball_dy = random.randint(-5, 5)
        update_score(score_a, score_b)
        wn.update()
        time.sleep(2)

    ball.setx(ball.xcor() + ball_dx)
    ball.sety(ball.ycor() + ball_dy)

    if ball.ycor() > ymax:
        ball.sety(ymax)
        ball_dy *= -1

    if ball.ycor() < ymin:
        ball.sety(ymin)
        ball_dy *= -1

    if ball.xcor() > xmax:
        score_a += 1
        point = True

    if ball.xcor() < xmin:
        score_b += 1
        point = True

    # test for collision with paddle a (left side)
    if ball.xcor() < pad_a_line + ball_size:
        if ball.xcor() > pad_a_line:
            if abs(pad_a.ycor() - ball.ycor()) < 60:
                ball.setx(pad_a_line + ball_size)
                ball_dx *= -1

    # test for collision with paddle b (right side)
    if ball.xcor() > pad_b_line - ball_size:
        if ball.xcor() < pad_b_line:
            if abs(pad_b.ycor() - ball.ycor()) < 60:
                ball.setx(pad_b_line - ball_size)
                ball_dx *= -1

    # loop end ---------------------
    time.sleep(max(1./30 - (time.time() - frame_start), 0))

# cleanup turtle window
turtle.bye()
