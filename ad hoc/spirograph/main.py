import turtle
from random import randint

pen = turtle.Turtle()
screen = turtle.Screen()

pen.speed("fastest")
screen.colormode(255)

circle_amount = 200
radius = 100

for i in range(circle_amount):
    pen.circle(radius)
    pen.right(360/circle_amount)
    pen.color(randint(0, 255), randint(0, 255), randint(0, 255))

screen.exitonclick()
