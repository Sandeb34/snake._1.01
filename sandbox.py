# *****NOTES ONLY*****

# my own interpretation on the challenge main.py
from turtle import Turtle, Screen

screen = Screen()
screen.setup(600,600)
screen.bgcolor("black")
screen.title("Snake eater")

new_segment = Turtle()

all_snake_parts = []
x_positions = [0, -20, -40]


for snake_index in range(0, 3):
    new_segment.penup()
    new_segment.color("white")
    new_segment.shape("square")
    # the end of the screen is 250 but turtles will not be visible therefor 230
    new_segment.goto(x=x_positions[snake_index],y=0)
    all_snake_parts.append(new_segment)



