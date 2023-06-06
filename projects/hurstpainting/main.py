import colorgram
import turtle
from random import choice

# initializing objects
pen = turtle.Turtle()
screen = turtle.Screen()

# setting pen properties
pen.speed("fastest")
pen.up()
pen.setx(-300)
pen.sety(250)

# screen properties
screen.colormode(255)

# drawing properties
radius = 15
space = 50
width = 10
height = 10

rgb_colors = []
colors = colorgram.extract('image.jpg', 20)

for color in colors:
    r = color.rgb.r
    g = color.rgb.g
    b = color.rgb.b
    new_color = (r, g, b)
    rgb_colors.append(new_color)

for row in range(height):
    for column in range(width):
        pen.color(choice(rgb_colors))
        pen.begin_fill()
        pen.forward(space)
        pen.circle(radius)
        pen.end_fill()
    pen.right(180)
    pen.forward(space*width)
    pen.left(90)
    pen.forward(space)
    pen.left(90)




screen.exitonclick()