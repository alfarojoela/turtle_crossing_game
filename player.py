from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self. penup()
        self.go_to_start()
        self.shape("turtle")
        self.color("black")
        self.setheading(90)

    def up(self):
        # new_y = self.ycor() + MOVE_DISTANCE
        # self.goto(self.xcor(), new_y)
        #SOLUTION uses object method of forward rather than using y coordinates and goto method.
        #appears to have similiar if not same result.
        self.forward(MOVE_DISTANCE)

        #code solution uses more methods and constants instead of hardcoded values.
    def go_to_start(self):
        self.goto(STARTING_POSITION)

    def is_at_finish_line(self):
        if self.ycor() > FINISH_LINE_Y:
            return True
        else:
            return False
