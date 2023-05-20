# main.py

import turtle
from game_constants import *
from game_objects import Ball, Slider, ScoreDisplay
from input_handlers import setup_input_handlers
from game_functions import move_ball, check_boundaries, check_score, check_collision

# Create the window
window = turtle.Screen()
window.title("Venus Pong")
window.bgcolor(WINDOW_BG_COLOR)
window.setup(width=WINDOW_WIDTH, height=WINDOW_HEIGHT)
window.tracer(0)

# Create game objects
ball = Ball()
slider_a = Slider(SLIDER_A_START_POS)
slider_b = Slider(SLIDER_B_START_POS)
score_display = ScoreDisplay()

# Setup input handlers
setup_input_handlers(window, slider_a, slider_b)

# Initial scores
score_a = SCORE_A_START
score_b = SCORE_B_START

# Main game loop
while True:
    window.update()

    move_ball(ball)
    check_boundaries(ball)
    score_a, score_b = check_score(ball, score_a, score_b, score_display)
    check_collision(ball, slider_a, slider_b)
