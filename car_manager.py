from turtle import Turtle, Screen
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10
TURTLE_LIST = []

class CarManager:
    def __init__(self):
        self.y = random.randint(-260, 260)
        self.x = 265
        self.move_x = -20
        self.length_list = 0
        turtle = Turtle()
        turtle.penup()
        turtle.shape("square")
        turtle.shapesize(1, 2)
        turtle.color(random.choice(COLORS))
        turtle.goto(self.x, self.y)
        TURTLE_LIST.append(turtle)
        self.length_list = len(TURTLE_LIST)

    def create_cars(self):
        print(self.y)
        turtle = Turtle()
        turtle.penup()
        turtle.shape("square")
        turtle.shapesize(1, 2)
        turtle.color(random.choice(COLORS))
        turtle.goto(self.x, self.y)
        TURTLE_LIST.append(turtle)
        self.length_list = len(TURTLE_LIST)

    def move_car(self):
        for car in range(self.length_list):
            TURTLE_LIST[car].forward(self.move_x)
        if TURTLE_LIST[self.length_list - 1].xcor() <= 255:
            self.y = random.randint(-260, 260)
            print(self.y)
            self.create_cars()
            print(TURTLE_LIST)






