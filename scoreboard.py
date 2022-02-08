from turtle import Turtle

FONT = ("Courier", 27, "normal")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.goto(-280, 260)
        self.level = 1
        self.new_level()


    def new_level(self):
        self.write(f"Level: {self.level}", align="left", font=FONT)
        self.level += 1

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", align="center", font=FONT)


