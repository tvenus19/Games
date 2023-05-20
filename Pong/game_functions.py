from assets import bounce_sound

def move_ball(ball):
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

def check_boundaries(ball):
    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1
        bounce_sound.play()
    elif ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *= -1
        bounce_sound.play()

def check_score(ball, score_a, score_b, score_display):
    if ball.xcor() > 390:
        ball.goto(0, 0)
        ball.dx *= -1
        score_a += 1
        score_display.update_score(score_a, score_b)

    elif ball.xcor() < -390:
        ball.goto(0, 0)
        ball.dx *= -1
        score_b += 1
        score_display.update_score(score_a, score_b)
    return score_a, score_b

def check_collision(ball, slider_a, slider_b):
    if (ball.dx > 0) and (340 < ball.xcor() < 350) and (slider_b.ycor() - 50 < ball.ycor() < slider_b.ycor() + 50):
        ball.color("blue")
        ball.dx *= -1
        bounce_sound.play()
    elif (ball.dx < 0) and (-340 > ball.xcor() > -350) and (slider_a.ycor() - 50 < ball.ycor() < slider_a.ycor() + 50):
        ball.color("red")
        ball.dx *= -1
        bounce_sound.play()
