# Creating a Reptile class as a child class of Animal class

from animal import Animal  # Syntax to import files and classes


class Reptile(Animal):
    def __init__(self):
        super().__init__()  # Super key word is used to inherit everything from a parent class
        self.cold_blooded = True
        self.tetrapod = True
        self.heart_chambers = [3, 4]

    # Creating functions for our Reptile class

    def seek_heat(self):
        return "Look for a warm place"

    def hunt(self):
        return "Go get that meal"

    def use_venom(self):
        return "If i've got it i'm using it"


# Lets create an object of our Reptile class to utilise the functionalities of OOP
# reptile_object = Reptile()
#
# print(reptile_object.eat()) # Using functions from parent class (Animal) to test the super().__init__()
# print(reptile_object.breathe())
# print(reptile_object.procreate())
#
# print(reptile_object.hunt()) # Using functions from Reptile
# print(reptile_object.seek_heat())
# print(reptile_object.use_venom())