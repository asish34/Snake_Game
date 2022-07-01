from turtle import Turtle
import random

class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.create()

    def create(self):
        self.color("blue")
        self.shape("circle")
        self.shapesize(stretch_len=.5,stretch_wid=.5)
        self.penup()
        self.goto(random.randint(-270,270),random.randint(-270,270))