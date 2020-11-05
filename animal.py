# Creating an Animal class as PARENT / BASE / SUPER class

class Animal:

    def __init__(self):  # initialising the Animal class
        self.alive = True  # Creating an attribute / variable
        self.spine = True
        self.lungs = True
        self.eyes = True

    # Create behaviours as functions / methods
    def breathe(self):
        return "Keep breathing to stay alive"

    def move(self):
        return "Left to right and up and down ..."

    def eat(self):
        return "Nom Nom Nom"

    def procreate(self):
        return "Find partner"


# Instantiate our class / create an object

# cat = Animal() # Creating an object of Animal class cat(child class) which has inherited everything from Animal
# # (# parent class)
# Abstrcted eat() method from our parent class
# print(cat.eat())
