from turtle import Turtle
from random import randint
class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_len=0.5,stretch_wid=0.5)
        self.color("blue")
        self.speed("fastest")
        self.refresh()
        #buraya refresh atmazsak food hep ortadan başlar.
    def refresh(self):
        x1 = randint(-280,280)
        y1 = randint(-280,280)
        self.goto(x1,y1)
