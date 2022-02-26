from turtle import Turtle


class Paddle(Turtle):
    def __init__(self, coordinates):
        super().__init__("square")
        self.color("white")
        self.penup()
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.x_pos = coordinates[0]
        self.y_pos = coordinates[1]
        self.coordinates = coordinates
        self.goto(self.coordinates)

    def move_up(self):
        if self.y_pos < 225:
            self.y_pos += 20
            self.goto(self.x_pos, self.y_pos)

    def move_down(self):
        if self.y_pos > -225:
            self.y_pos -= 20
            self.goto(self.x_pos, self.y_pos)

    def get_coordinates(self):
        return self.x_pos, self.y_pos;

