#Import potrebnih modula

import turtle
import simpleaudio as sa

#Ucitavanje zvuka iz file-a u folderu
bounce_sound = sa.WaveObject.from_wave_file("bounce.wav")

#Stvaranje prozora na ekranu
window = turtle.Screen()
window.title("Venus Pong")
window.bgcolor("black")
window.setup(width=800, height=600)
window.tracer(0)

# Varijable za kasnije pracenje score-a
score_a = 0
score_b = 0

#Prikaz Slider A
slider_a = turtle.Turtle()
slider_a.speed(0)
slider_a.shape("square")
slider_a.color("white")
slider_a.shapesize(stretch_wid=5, stretch_len=1)
slider_a.penup()
slider_a.goto(-350, 0)


#Prikaz Slider B
slider_b = turtle.Turtle()
slider_b.speed(0)
slider_b.shape("square")
slider_b.color("white")
slider_b.shapesize(stretch_wid=5, stretch_len=1)
slider_b.penup()
slider_b.goto(350, 0)

#Prikaz lopte
lopta = turtle.Turtle()
lopta.speed(0)
lopta.shape("square")
lopta.color("white")
lopta.penup()
lopta.goto(0, 0)
lopta.dx = 0.2
lopta.dy = 0.2

# Pen prikaz score-a
pen = turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto (0,260)
pen.write("Player A: 0  PlayerB: 0", align="center", font=("Courier", 24, "normal"))


#Funkcije za pomicanje slidera
def slider_a_up():
    y = slider_a.ycor()
    y += 20
    slider_a.sety(y)

def slider_a_down():
    y = slider_a.ycor()
    y -= 20
    slider_a.sety(y)

def slider_b_up():
    y = slider_b.ycor()
    y += 20
    slider_b.sety(y)

def slider_b_down():
    y = slider_b.ycor()
    y -= 20
    slider_b.sety(y)

#Keyboard binding
window.listen()
window.onkeypress(slider_a_up, "w")
window.onkeypress(slider_a_down, "s")
window.onkeypress(slider_b_up, "Up")
window.onkeypress(slider_b_down, "Down")


#Main game loop
while True:
    window.update()

    #Pokreci loptu
    lopta.setx(lopta.xcor() + lopta.dx)
    lopta.sety(lopta.ycor() + lopta.dy)

    # Chekiranje granica igre
    if lopta.ycor() > 290:
        lopta.sety(290)
        lopta.dy *= -1
        bounce_sound.play()


    if lopta.ycor() < -290:
        lopta.sety(-290)
        lopta.dy *= -1
        bounce_sound.play()

    #Chekiranje jel postignut gol i update score-a

    if lopta.xcor() > 390:
        lopta.goto(0,0)
        lopta.dx *= -1
        score_a += 1
        pen.clear()
        pen.write("Player A: {}  PlayerB: {}".format(score_a, score_b), align="center", font=("Courier", 24, "normal"))

    if lopta.xcor() < -390:
        lopta.goto(0,0)
        lopta.dx *= -1
        score_b += 1
        pen.clear()
        pen.write("Player A: {}  PlayerB: {}".format(score_a, score_b), align="center", font=("Courier", 24, "normal"))
        

    #Sudaranje lopte i slidera
    if (lopta.xcor() > 340 and lopta.xcor() < 350) and (lopta.ycor() < slider_b.ycor() + 51 and lopta.ycor() > slider_b.ycor() -51):
        lopta.setx(340)
        lopta.dx *= -1
        bounce_sound.play()

    if (lopta.xcor() < -340 and lopta.xcor() > -350) and (lopta.ycor() < slider_a.ycor() + 51 and lopta.ycor() > slider_a.ycor() -51):
        lopta.setx(-340)
        lopta.dx *= -1
        bounce_sound.play()