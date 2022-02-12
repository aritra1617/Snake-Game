from turtle import Turtle
STARTING_POS = [(0, 0), (-20, 0), (-40, 0)]
MOV_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:
    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]

    def create_snake(self):
        for pos in STARTING_POS:
            self.segment(pos)

    def position(self):
        return (self.xcor(), self.ycor())

    def segment(self, pos):
        seg = Turtle("square")
        seg.penup()
        seg.color("white")
        seg.goto(pos)
        self.segments.append(seg)

    def extend(self):
        self.segment(self.segments[-1].position())

    def move(self):
        for idx in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[idx - 1].xcor()
            new_y = self.segments[idx - 1].ycor()
            self.segments[idx].goto(new_x, new_y)
        self.segments[0].forward(MOV_DISTANCE)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)
