from turtle import Turtle
from game_constants import *

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.speed(BALL_SPEED)
        self.shape(BALL_SHAPE)
        self.color(BALL_COLOR)
        self.penup()
        self.goto(BALL_START_POS)
        self.dx = BALL_DX
        self.dy = BALL_DY

class Slider(Turtle):
    def __init__(self, start_pos):
        super().__init__()
        self.speed(SLIDER_SPEED)
        self.shape(SLIDER_SHAPE)
        self.color(SLIDER_COLOR)
        self.shapesize(stretch_wid=SLIDER_STRETCH_WID, stretch_len=SLIDER_STRETCH_LEN)
        self.penup()
        self.goto(start_pos, 0)

    def go_up(self):
        y = self.ycor()
        y += 20
        self.sety(y)

    def go_down(self):
        y = self.ycor()
        y -= 20
        self.sety(y)

class ScoreDisplay(Turtle):
    def __init__(self):
        super().__init__()
        self.speed(0)
        self.color("white")
        self.penup()
        self.hideturtle()
        self.goto(0, 260)
        self.update_score(SCORE_A_START, SCORE_B_START)

    def update_score(self, score_a, score_b):
        self.clear()
        self.write(f"Player A: {score_a}  Player B: {score_b}", align="center", font=SCORE_FONT)
