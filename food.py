from turtle import Turtle
import random


class Food(Turtle):

    def __init__(self):
        """Adds attributes to the Food class"""
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)  # Resize the food by half (*0.5)
        self.color("blue")
        self.speed("fastest")
        random_x = random.randint(-280, 280)
        random_y = random.randint(-280, 280)
        self.goto(random_x, random_y)
        self.refresh()    # Put food in new location

    def refresh(self):
        """Puts food in new location"""
        score = 0
        random_x = random.randint(-280, 280)
        random_y = random.randint(-280, 280)
        self.goto(random_x, random_y)
        score += 1
