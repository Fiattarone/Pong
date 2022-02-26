from turtle import Turtle


class Scorebrain(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.leftscore = 0
        self.rightscore = 0
        self.write_scores()

    def write_scores(self):
        self.clear()
        self.goto(-100, 200)
        self.write(self.leftscore, align="center", font=("Courier", 80, "normal"))
        self.goto(100, 200)
        self.write(self.rightscore, align="center", font=("Courier", 80, "normal"))

    def increase_score(self, num, str):
        if (str == "left"):
            self.leftscore += num
        elif (str == "right"):
            self.rightscore += num

        self.write_scores()

