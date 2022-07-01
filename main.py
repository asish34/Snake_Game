from turtle import Turtle,Screen
from snake import Snake
import time
from food import Food
from score_board import  Score_Board

my_screen=Screen()
my_screen.bgcolor("black")
my_screen.setup(width=600,height=600)
my_screen.listen()
my_screen.tracer(0)



snake=Snake()

food=Food()
score=Score_Board()

my_screen.onkey(snake.up,"Up")
my_screen.onkey(snake.down,"Down")
my_screen.onkey(snake.left,"Left")

my_screen.onkey(snake.right,"Right")
is_game_on=True

while is_game_on:
    time.sleep(.1)
    my_screen.update()
    snake.move()

    # Collison with food
    if(snake.head.distance(food)<15):
        food.hideturtle()
        food.create()
        food.showturtle()
        score.update_score()
        snake.extend(snake.segments[-1].position())
    if snake.head.xcor()>270 or snake.head.ycor()>270 or snake.head.xcor()<-270 or snake.head.ycor()<-270:
        is_game_on=False
        score.game_over()
    for si in snake.segments[1:len(snake.segments)]:
        if(snake.head.distance(si)<10):
            is_game_on=False
            score.game_over()    


my_screen.exitonclick()