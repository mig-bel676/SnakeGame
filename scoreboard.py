from turtle import Turtle
ALIGNMENT = "center"
FONT = ('Arial', 24, 'normal')
POSITION = (0, 260)


class Score(Turtle):
    def __init__(self):
        super().__init__()
        # This is retrieving data from file and opening it while object is initializing
        with open("high_score_data.txt") as data:
            self.highscore = int(data.read())
        self.pencolor("white")
        self.penup()
        self.hideturtle()
        self.score = 0
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.goto(POSITION)
        self.write(f"Score: {self.score}    High Score: {self.highscore}", move=True, align=ALIGNMENT, font=FONT)

    def update_score(self):
        self.score += 1
        self.update_scoreboard()

    def reset_score(self):
        if self.score > self.highscore:
            self.highscore = self.score
            with open("high_score_data.txt", mode="w") as data:
                data.write(f"{self.score}")
        self.score = 0
        self.update_scoreboard()



