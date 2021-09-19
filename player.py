from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self. penup()
        self.setposition(STARTING_POSITION)
        self.shape("turtle")
        self.color("black")
        self.setheading(90)

    def up(self):
        new_y = self.ycor() + 20
        self.goto(self.xcor(), new_y)

    def down(self):
        new_y = self.ycor() - 20
        self.goto(self.xcor(), new_y)

    def right(self):
        new_x = self.xcor() +20
        self.goto(new_x, self.ycor())

    def left(self):
        new_x = self.xcor() -20
        self.goto(new_x, self.ycor())