from turtle import Turtle
FONT=('Arial', 20, 'normal')
class Scorecard(Turtle):
    def __init__(self):
        super(Scorecard, self).__init__()
        self.score=0
        with open("data.txt",mode="r") as file:
            self.high_score=int(file.read())
        self.hideturtle()
        self.color("White")
        self.penup()
        self.goto(0,270)
        self.score_update()
    def game_over(self):
        self.goto(0,0)
        self.reset()
        self.write("GAME OVER",align="center",font=FONT)
    def score_update(self):
        self.clear()
        self.write(f"Your Score {self.score}       HighScore: {self.high_score}", align="center", font=FONT)
        self.score=self.score+1
    def reset(self):
        if self.score>self.high_score:
            self.high_score=self.score
            with open("data.txt",mode="w") as file:
                file.write(f"{self.high_score}")