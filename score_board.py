from turtle import Turtle

class Score_Board(Turtle):
    def __init__(self):
        super().__init__()
        self.score=0
        self.goto(0,260)
        self.hideturtle()
        self.penup()
        self.color("white","white")
        self.update()

    def update(self):
        self.write(f'Score : {self.score}',align="center",font=("Arial",27,"normal"))
    
    def update_score(self):
        self.clear()
        self.score+=1
        self.update()
        
    
    def game_over(self):
        self.clear()
        self.write('Game over',align="center",font=("Arial",27,"normal"))
