from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager(Turtle):
    def __init__(self, speed):
        super().__init__()
        self.penup()
        self.shape("square")
        self.color(random.choice(COLORS))
        self.shapesize(stretch_wid=1, stretch_len=2)
        self.y_position = random.randint(-250, 250)
        self.setposition(280, self.y_position)
        self.x_move = -10
        self.y_move = 0
        self.move_speed = speed

    #had written below previously as new_x =(self.xcor() -MOVE_INCREMENT) * self.move_speed but cars moved
    #erratically.  below appears to work better as the MOVE_INCREMENT is increased before being subtracted from
    #present x coordinates.
    def move(self):
        new_x = self.xcor() - (MOVE_INCREMENT * self.move_speed)
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)

    def increment_speed(self):
        self.move_speed += 0.25



