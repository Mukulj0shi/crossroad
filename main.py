import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
carmanager = CarManager()
#Create first car

game_is_on = True
while game_is_on:
    time.sleep(1)
    screen.update()
    #Make cars move in the screen
    carmanager.move_car()


screen.exitonclick()
