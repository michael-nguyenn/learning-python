# Class Inheritance

# Suppose we create a robot chef that has general functions
#   Aka bake(), stir(), measure()
#   But now we want to add extra functionality
#       This can be done via inheritance


class Animal:
    def __init__(self):
        self.num_eyes = 2
        self.oxygen = 0

    def breathe(self):
        print("Inhale... Exhale...")
        self.oxygen += 1


# CLASS INHERITANCE
class Fish(Animal):
    def __init__(self):
        super().__init__()
        self.distance = 0

    def swim(self):
        print("Swim swim swim...")
        self.distance += 1

    def breathe(self):
        super().breathe()
        print("doing this underwater")


nemo = Fish()
print(nemo.distance)
nemo.swim()
print(nemo.distance)
nemo.breathe()
print(nemo.num_eyes)
