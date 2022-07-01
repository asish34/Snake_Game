from turtle import Turtle
cordinates=[(0,0),(-20,0),(-40,0)]
UP=90
DOWN=270
LEFT=180
RIGHT=0

class Snake:
    def __init__(self):
        self.segments=[]
        self.create()
        self.head=self.segments[0]

    def create(self):
        for i in range(0,3):
            self.extend(cordinates[i])

    def extend(self,p):
            snake=Turtle(shape="square")
            snake.penup()
            snake.speed("fast")
            snake.color("white","white")
            snake.goto(p)
            self.segments.append(snake)




    def move(self):
        for i in range(len(self.segments)-1,0,-1):
            xa=self.segments[i-1].xcor()
            ya=self.segments[i-1].ycor()
            self.segments[i].goto(x=xa,y=ya)
        self.head.fd(20)


    def up(self):
        if self.head.heading()!=DOWN:
            self.head.setheading(UP)
    def down(self):
         if self.head.heading()!=UP:
            self.head.setheading(DOWN)
    def left(self):
        if self.head.heading()!=RIGHT:
            self.head.setheading(LEFT)
    def right(self):
        if self.head.heading()!=LEFT:
            self.head.setheading(RIGHT)       
