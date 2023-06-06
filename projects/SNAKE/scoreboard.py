from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.hideturtle()
        self.penup()
        self.goto(0, 270)
        self.color("white")
        self.write(f"Your Score: {self.score}", align="center", font=("Ariel", 24, "normal"))

    def scoreboard(self):
        self.clear()
        self.score += 1
        self.write(f"Your Score: {self.score}", align="center", font=("Ariel", 24, "normal"))

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", align="center", font=("Ariel", 24, "normal"))
