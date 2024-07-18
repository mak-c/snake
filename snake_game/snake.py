import time
from turtle import Turtle

STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
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
        for position in STARTING_POSITIONS:
            self.add_segment(position)

    def add_segment(self, position):
        new_segment = Turtle("square")
        new_segment.color("white")
        new_segment.penup()
        new_segment.goto(position)
        self.segments.append(new_segment)

    def reset(self):
        for seg in self.segments:
            seg.reset()
        self.segments.clear()
        self.create_snake()
        self.head = self.segments[0]

    def extend(self):
        self.add_segment(self.segments[-1].position())

    def move(self):
        for seg_num in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[seg_num - 1].xcor()
            new_y = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(new_x, new_y)
        self.segments[0].forward(MOVE_DISTANCE)

#   #this code fixes the issue of fast inputs making the snake double back on itself. Checks that the snake head does
#   #not have to same x or y position of the following segment (segments[1]), if it does not, then direction is changed
    def up(self):
        if self.segments[0].ycor() + MOVE_DISTANCE != self.segments[1].ycor():
            self.head.setheading(UP)

    def down(self):
        if self.segments[0].ycor() - MOVE_DISTANCE != self.segments[1].ycor():
            self.head.setheading(DOWN)

    def left(self):
        if self.segments[0].xcor() - MOVE_DISTANCE != self.segments[1].xcor():
            self.head.setheading(LEFT)

    def right(self):
        if self.segments[0].xcor() + MOVE_DISTANCE != self.segments[1].xcor():
            self.head.setheading(RIGHT)

#   #code has bug of quick inputs causing snake to go back on itself
# def up(self):
#     if self.head.towards(self.segments[1]) != DOWN:
#         time.sleep(0.1)
#         self.head.setheading(UP)
#
# def down(self):
#     if self.head.towards(self.segments[1]) != UP:
#         time.sleep(0.1)
#         self.head.setheading(DOWN)
#
# def left(self):
#     if self.head.towards(self.segments[1]) != RIGHT:
#         time.sleep(0.1)
#         self.head.setheading(LEFT)
#
# def right(self):
#     if self.head.towards(self.segments[1]) != LEFT:
#         time.sleep(0.1)
#         self.head.setheading(RIGHT)
