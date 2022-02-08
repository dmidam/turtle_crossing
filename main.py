import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()
scoreboard = Scoreboard()

cars = []

screen.listen()
screen.onkeypress(player.move, "Up")

turns = 0
game_is_on = True
while game_is_on:
    turns += 1
    time.sleep(0.1)
    screen.update()
    if turns % 6 == 0:
        car_manager = CarManager()
        cars.append(car_manager)
    for car in cars:
        car.car_move()
    for cur in cars:
        if player.distance(cur) < 26:
            scoreboard.game_over()
            game_is_on = False
    if player.ycor() > 280:
        car_manager.acceleration()
        player.goto(0, -280)
        scoreboard.clear()
        scoreboard.new_level()

screen.exitonclick()
