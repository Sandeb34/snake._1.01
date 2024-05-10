from turtle import Turtle, Screen
# Constant variables
# Tweak variables here:
STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


# __init__(self): is used for attributes
class Snake:
    # What will happen when we initialize a new snake object.
    def __init__(self):
        """Add Attributes for Snake class"""
        # New ATTRIBUTES (has)
        self.segments = []
        self.create_snake()
        # first segment is list is snake's head
        self.head = self.segments[0]

    # METHOD because it does
    def create_snake(self):
        """Creates a 3-segment snake"""
        for position in STARTING_POSITIONS:
            self.add_segment(position)

    def add_segment(self, position):
        new_segment = Turtle(shape="square")
        new_segment.color("white")
        new_segment.penup()
        new_segment.goto(position)
        self.segments.append(new_segment)

    def reset(self):
        # move snake segments off the screen
        for seg in self.segments:
            seg.goto(1000,1000)
        # deletes list with snake segments
        self.segments.clear()
        self.create_snake()
        self.head = self.segments[0]

    def extend(self):
        """add a new segment to the snake after eating"""
        self.add_segment(self.segments[-1].position())  # -1 starts counting at the end of the list
    #     add new segment to kast position

    def move(self):
        """Moves the segments of the snake each segment taking the coordinate
        of the previous segment except segment 1st """
        for seg_numb in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[seg_numb - 1].xcor()
            new_y = self.segments[seg_numb - 1].ycor()
            self.segments[seg_numb].goto(new_x, new_y)
        self.head.forward(MOVE_DISTANCE)

    def up(self):
        # If current heading pointed "down" cant move "up".
        # Heading as method so use ( ) to check value with constant variables DOWN, UP, RIGHT, and LEFT.
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)





