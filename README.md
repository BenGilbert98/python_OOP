# Python OOP
**Step 1**
- Creating an Animal class as our Parent
```
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
```
**Step 2** 
- Creating Reptile class as a child class
- To inherit from Animal class which is parent class
- Abstract
```
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
```
**Step 3**
-  Create Snake class as child of Reptile
```
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
```
**Step 4**
- Create a Python class as a child of Snake
```
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
```
- ```__name__``` and ```__main__``` are used to check if the code is run from the current file / directory for different file / importing it
- we will create 2 files and use ```__name__``` and ```__main__``` in both files and the outcome will show the difference 

# Getter and Setters
```
class Student:
    def __init__(self, name, company):
        self.name = name
        self.company = company


    def getStudent(self, value):
        self.__name # __ are used to hide the data

    def setStudent(self, value):
        self.__name = value

student_object = Student("Ben", "Sparta Global")

print(f"Student name is {student_object.setStudent()}")
```

**Second Iteration**
```
class Student:
    def __init__(self, name, company):
        self.name = name
        self.company = company

    @property # A decorator in python is any callable python object that is used to modify a function or a class
    def Student(self, value):
        print(" This setter method in student data")
        self.__name # __ are used to hide the data
```
- A decorator in python is any callable python object that is used to modify a function or a class
```
    @Student.setter
    def Student(self, value):
        print(" Calling @student.student method")
        self.__name = value
```
- Creating an object with required information
```
student_object = Student("Ben", "Sparta Global")

print(f"Student name is {student_object.name}")
print("=" * 34)
print(f"Student works in {student_object.company}")
```
