from turtle import Screen
#Turtle ı daha burda kullanmıyoz o yüzden sildik
from snake import Snake
import time 
from food import Food
from scoreboard import ScoreBoard
s = Screen()
s.setup(width=600,height=600)
s.bgcolor("black")
s.title("My Snake Game")
s.tracer(0)

food = Food()
snake = Snake()
sb = ScoreBoard()

s.listen()
s.onkey(snake.upp,"Up")
s.onkey(snake.down,"Down")
s.onkey(snake.left,"Left")
s.onkey(snake.right,"Right")

is_game_on=True
while is_game_on:
    s.update()
    time.sleep(0.1)
    snake.move()

    if snake.head.distance(food)<15:
        print("nomnomnom")
        food.refresh()
        sb.inc_scor_count()
        snake.extend()
    if snake.head.xcor() > 280 or snake.head.xcor() < -300 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        is_game_on = False
        sb.game_over()
    for segment in snake.segments:
        if segment == snake.head:
            pass
        #baya güzel yöntem düşünemedin
        elif snake.head.distance(segment) < 20 :
            is_game_on = False
            sb.game_over()
            
    
s.exitonclick()









