import random
from turtle import Turtle
class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.speed("fastest")
        self.color("blue")
        self.shapesize(stretch_len=0.5,stretch_wid=0.5)
        self.refresh()
    def refresh(self):
        x_cor = random.randint(-280, 280)
        y_cor = random.randint(-280, 280)
        cordinate = (x_cor, y_cor)
        self.goto(cordinate)


