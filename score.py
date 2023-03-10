from turtle import Turtle


class Score(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.hideturtle()
        self.penup()
        self.goto(0, 260)
        self.update_score()

    def update_score(self):     # Update score?
        self.write(f"Score: {self.score}", align= "center", font= ("Arial", 20, "normal"))

    def add_score(self):
        self.score += 1
        self.clear()
        self.write(f"Score: {self.score}", align="center", font=("Arial", 20, "normal"))

