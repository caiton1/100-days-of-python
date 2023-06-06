import turtle
import random

pen = turtle.Turtle()
screen = turtle.Screen()
screen.listen()


def move_forward():
    pen.forward(10)


def move_backwards():
    pen.backward(10)


def move_right():
    pen.right(10)


def move_left():
    pen.left(10)

def clear():
    pen.setheading(0)
    pen.home()
    pen.clear()


screen.onkey(key="a", fun=move_left)
screen.onkey(key="d", fun=move_right)
screen.onkey(key="w", fun=move_forward)
screen.onkey(key="s", fun=move_backwards)
screen.onkey(key="c", fun=clear)

screen.exitonclick()
