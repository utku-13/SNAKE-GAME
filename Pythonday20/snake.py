STARTING_POS =[(0,0),(-20,0),(-40,0)]
from turtle import Turtle
MOVE_DISTANCE=20
UP = 90
RIGHT = 0 
LEFT = 180
DOWN = 270
class Snake:
    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]

    def create_snake(self):
        for position in STARTING_POS:
            self.add_segment(position)
    
    def add_segment(self, position):
        t1 = Turtle(shape="square")
        t1.color("white")
        t1.penup()
        t1.goto(position)
        self.segments.append(t1)

    def extend(self):
        self.add_segment(self.segments[-1].position())



    def move(self):
        for seg in range(len(self.segments)-1,0,-1):
            x1= self.segments[seg-1].xcor()
            y1= self.segments[seg-1].ycor()
            self.segments[seg].goto(x=x1,y=y1)
        self.head.forward(MOVE_DISTANCE)
        
    def upp(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)
    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)
    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)
    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)




