# Creating Python class as a child of Snake
from snake import Snake


class Python(Snake):

    def __init__(self):
        super().__init__()
        self.large = True
        self.two_lungs = True
        self.venom = False

    # Creating functions for our Python class

    def digest_large_prey(self):
        return "Swallows large prey"


    def climb(self):
        return "Up we go ... "


    def shed_skin(self):
        return "Time to shed skin"

# Create object / instance of this class
python_object = Python()

print(python_object.breathe()) # From Animal parent class
print(python_object.hunt()) # From Reptile parent class
print(python_object.use_tongue_to_smell()) # From Snake parent class
print(python_object.climb()) # From Python class

