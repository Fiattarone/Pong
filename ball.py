import random
from turtle import Turtle
from random import randint


class Ball(Turtle):
    def __init__(self):
        super().__init__("circle")
        self.shapesize(stretch_wid=1, stretch_len=1)
        self.color("white")
        self.penup()
        self.goto(0, 0)
        self.setheading(randint(0, 360))

    def check_collision(self, paddle):
        if (self.distance(paddle) < 50 and self.xcor() > 320) or (self.distance(paddle) < 50 and self.xcor() < -320):
            if self.distance(paddle) < 25 and (self.heading() < 90 or self.heading() > 270):
                if self.distance(paddle) > 5:
                    self.setheading(randint(135, 225))
                    print("Less than 20!")
            elif self.distance(paddle) < 25 and (90 < self.heading() < 270):
                if self.distance(paddle) > 5:
                    temp = randint(-45, 45)
                    if temp < 0:
                        self.setheading(temp+360)
                    else:
                        self.setheading(temp)
                    print("Less than 20 left!")
                else:
                    print(self.heading())
                    self.setheading(180 - self.heading())
            else:
                #50 is angled steep, fix later.
                print(self.heading())
                self.setheading(180-self.heading())

    def check_wall_collision(self):
        if self.ycor() > 300 or self.ycor() < -300:
            print(f"Heading is {self.heading()}")
            self.setheading(360 - self.heading())

    def check_left_goal(self):
        if self.xcor() < -400:
            return True
        return False
    #         left player wins

    def check_right_goal(self):
        if self.xcor() > 400:
            return True
        return False
    #         right player wins

    def move(self):
        self.forward(10)

    def reset(self):
        self.goto(0, 0)
        tuple_holder = (randint(-50, 50), randint(130, 230))
        self.setheading(random.choice(tuple_holder))
