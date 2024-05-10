# *****NOTES ONLY*****

# Old school snake game
# ****THIS FILE IS BEFORE IMPLEMENTED CLASSE TO SHOWCASE TOUGHT PROCESS****
from turtle import Screen, Turtle
import time

screen = Screen()
screen.setup(600,600)
screen.bgcolor("black")
screen.title("Snake eater")
screen.tracer(0)

# Add a list of tuples (fixed numbers)
starting_positions = [(0,0),(-20,0),(-40,0)]

segments = []
# Create_Snake Class
for position in starting_positions:
    new_segment = Turtle(shape="square")
    new_segment.color("white")
    new_segment.penup()
    new_segment.goto(position)
    segments.append(new_segment)

# Create_Move Class
game_is_on = True

while game_is_on:
    #   2. Refreshes screen after delay
    screen.update()
    #   1. Delay for 0.1 second
    time.sleep(0.1)

    #   1.  Starting_positions = [(0,0),(-20,0),(-40,0)]
    #   2.  These are starting positions of the segments
    #   3.  We move from 2-1-0 (as the positions from the list shown above in#1
    #   4.  Range takes the length of the (new) segments - 1 because of the positions in the list
    #   5.  Example segment number 6 is in position number 5 in the list because list starts at "0"
    for seg_numb in range(len(segments) - 1, 0, -1):
        # Second to last segment
        new_x = segments[seg_numb - 1].xcor()
        new_y = segments[seg_numb - 1].ycor()
        # Segment follows the predecessors' coordinates
        segments[seg_numb].goto(new_x, new_y)
    segments[0].forward(20)





screen.exitonclick()