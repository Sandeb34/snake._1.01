# *****NOTES ONLY*****

# Classes inheritance
# Lesson create classes within a class that can inherit attributes and methods
# *****THESE ARE **NOT** CLASSES USED IN THE SNAKE GAME******


class Animal:
    def __init__(self):
        self.num_eyes = 2

    def breathe(self):
        print("Inhale and exhale")


class Fish(Animal):
    def __init__(self):    # Here the attributes and methods are inherited by the Fish class.
        # The above code is not necessary but recommended.
        super().__init__()   # Use super to refer to 'main' Class or 'parent Class

    def breathe(self):
        super().breathe()      # Call from the super(). Class breathe() method
        print("doing this under water")  # Here it is modified by adding a string

    def swim(self):
        print("moving in the water")


nemo = Fish()
nemo.breathe()
