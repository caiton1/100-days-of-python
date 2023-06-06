import turtle
import random

screen = turtle.Screen()
screen.setup(width=500, height=400)

user_bet = screen.textinput(title="make your bet", prompt="What color will win? (red/blue/pink/black/purple/yellow): ")
is_race_on = False


turtles = []
colors = ["red", "blue", "purple", "pink", "black", "yellow"]
y_pos = [-70, -40, -10, 20, 50, 80]

starting_height = 1
for turtle_index in range(0,6):
    new_turtle = turtle.Turtle(shape="turtle")
    new_turtle.penup()
    new_turtle.color(colors[turtle_index])
    new_turtle.goto(x=-230, y=y_pos[turtle_index])
    turtles.append(new_turtle)

if user_bet:
    is_race_on = True

while is_race_on:
    for turtle in turtles:
        if turtle.xcor() > 230:
            winning_color = turtle.pencolor()
            is_race_on = False

        rand_distance = random.randint(0,10)
        turtle.forward(rand_distance)

if user_bet == winning_color:
    print(f"You've won. The {winning_color} turtle won.")
else:
    print(f"You loose. The {winning_color} turtle won")

screen.exitonclick()
