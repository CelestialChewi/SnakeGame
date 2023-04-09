from turtle import Turtle


class Score(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        with open("highscore.txt") as highscore:
            self.highscore = int(highscore.read())
        self.color("white")
        self.hideturtle()
        self.penup()
        self.goto(0, 260)
        self.update_score()

    def update_score(self):
        self.clear()
        self.write(f"Score: {self.score} High Score: {self.highscore}", align= "center", font= ("Arial", 20, "normal"))

    def reset(self):
        if self.score > self.highscore:
            self.highscore = self.score
            with open("highscore.txt", mode="w") as highscore:
                highscore.write(f"{self.highscore}")
        self.score = 0
        self.update_score()

    def add_score(self):
        self.score += 1
        self.update_score

