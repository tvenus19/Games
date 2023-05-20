from config import window
from game_objects import Ball, Slider, ScoreDisplay
from game_functions import move_ball, bounce_ball, score_point
from input_handlers import slider_a_up, slider_a_down, slider_b_up, slider_b_down

# Main game loop
while True:
    window.update()

    # Move the ball
    move_ball(ball)

    # Bounce the ball
    bounce_ball(ball, slider_a, slider_b)

    # Score a point
    score_point(ball, slider_a, slider_b, score_display)

    # Handle input
    window.listen()
    window.onkeypress(slider_a_up, "w")
    window.onkeypress(slider_a_down, "s")
    window.onkeypress(slider_b_up, "Up")
    window.onkeypress(slider_b_down, "Down")
