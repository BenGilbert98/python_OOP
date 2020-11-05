# Creating a Snake class as a child class of Reptile

from reptile import Reptile


class Snake(Reptile):
    def __init__(self):
        super().__init__()
        self.forked_tongue = True
        self.venom = True
        self.limbs = False

    # Creating functions for our Snake class
    def use_tongue_to_smell(self):
        return "I use tongue to taste the air"


# Create object of this class
# snake_object = Snake()
#
# print(snake_object.limbs) # From Snake class
# print(snake_object.eat()) # From Animal class
# print(snake_object.breathe())
# print(snake_object.hunt()) # From Reptile class

# We have double inheritance and Encapsulated in functions within parent classes
