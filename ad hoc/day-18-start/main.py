from turtle import Turtle, Screen
import random
from random_walk import RandomWalk

def draw_shape(num_sides):
    angle = 360/num_sides
    for i in range(num_sides):
        pen.forward(100)
        pen.right(angle)

pen = Turtle()


pen.shape("turtle")

for shape_sides in range(3,11):
    draw_shape(shape_sides)


RandomWalk.random_walk(length=100)
screen = Screen()
screen.exitonclick()

