import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

game_is_on = True

#put objects here
player = Player()
scoreboard= Scoreboard()

#screen listening here
screen.listen()
screen.onkey(player.up, "Up")
screen.onkey(player.down, "Down")
screen.onkey(player.right, "Right")
screen.onkey(player.left, "Left")



car_list =[]

game_loop =1
while game_is_on:
    time.sleep(0.1)
    screen.update()

    if game_loop == 6:
        car_object = CarManager()
        car_list.append(car_object)
        game_loop = 1

    for car in car_list:
        car.move()
        if car.xcor() < -500:
            car.hideturtle()
            car.clear()
            car_list.remove(car)

        if player.distance(car) < 15:
            game_is_on = False
            scoreboard.game_over()

        if player.ycor() >=300:
            player.setposition((0, -280))
            scoreboard.increment_level()
            # for cars in car_list:
            #     cars.increment_speed()



    game_loop += 1






screen.exitonclick()