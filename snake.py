from turtle import Turtle

STARTING_POSITION = [(0,0), (-20,0), (-40,0)]
class Snake:

    def __init__(self): # My snake
        self.segments = []
        self.make_snake()
        self.head = self.segments[0]

    def make_snake(self): # Make snake body
        for position in STARTING_POSITION:
            new_segment = Turtle()
            new_segment.shape("square")
            new_segment.color("white")
            new_segment.shapesize(1)
            new_segment.penup()
            new_segment.goto(position) # 3 segments coordinate
            self.segments.append(new_segment)

    def add_segment(self, position):
        new_segment = Turtle()
        new_segment.shape("square")
        new_segment.color("white")
        new_segment.shapesize(1)
        new_segment.penup()
        new_segment.goto(position)
        self.segments.append(new_segment)

    def reset(self):
        for segment in self.segments:
            segment.goto(1000,1000)
        self.segments.clear()
        self.make_snake()
        self.head = self.segments[0]

    def extend(self):
        self.add_segment(self.segments[-1].position())

    def move(self): # move the butt to head segment by segment
        for segment_number in range(len(self.segments) - 1, 0, -1):
            new_xcor = self.segments[segment_number - 1].xcor()
            new_ycor = self.segments[segment_number - 1].ycor()
            self.segments[segment_number].goto(new_xcor, new_ycor)
        self.head.forward(20)

    def left(self):
        if self.head.heading() != 0:
            self.head.setheading(180)

    def right(self):
        if self.head.heading() != 180:
            self.head.setheading(0)

    def up(self):
        if self.head.heading() != 270:
            self.head.setheading(90)

    def down(self):
        if self.head.heading() != 90:
            self.head.setheading(270)
