from turtle import Turtle

class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.score=0
        self.hideturtle()
        self.penup()
        self.goto(0,280)
        self.update_scoreboard()
    def update_scoreboard(self):
        self.write(f"score is {self.score}",move=False,align="center",font=('Arial', 15, 'normal'))
    def game_over(self):
        self.goto(0,0)
        self.write(f"GAME OVER",move=False,align="center",font=('Arial', 15, 'normal'))

    
    
    def inc_scor_count(self):
        self.clear()
        self.score += 1
        self.update_scoreboard()