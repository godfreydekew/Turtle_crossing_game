import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
level = 0
player = Player()
screen.listen()
screen.onkey(player.go_up, "Up")
game_is_on = True
score = Scoreboard()
car_manager = CarManager()

while game_is_on:
    time.sleep(0.1)
    screen.update()
    car_manager.create_car()
    car_manager.move_cars()
#detect collision with car
    for car in car_manager.all_cars:

        if player.distance(car) < 24:
            score.gameover()

            game_is_on = False
    #check if car arrived to the finish line
    if player.ycor() > 270:
        player.goto(0, -280)
        car_manager.levelup()
        score.update_score()

screen.exitonclick()
