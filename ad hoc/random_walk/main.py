import turtle
from random import choice, randint

pen = turtle.Turtle()
screen = turtle.Screen()


def rnadom_color():
    r = randint(0,255)
    g = randint(0,255)
    b = randint(0,255)
    random_color = (r, g, b)
    return random_color

screen.colormode(255)
pen.pensize(15)
pen.speed("fastest")

length = 200
pen_directions = [0, 90, 180, 270]
pen_colors = ["blue", "green", "red", "purple", "black", "pink"]

for i in range(length):
    pen.forward(25)
    pen.pencolor(randint(0,255), randint(0,255), randint(0,255))
    pen.setheading(choice(pen_directions))

screen.exitonclick()
