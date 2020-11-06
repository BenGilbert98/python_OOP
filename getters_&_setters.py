# Getter and Setters
# why - use cases
# to hide the data - separation of concern

# Syntax 2 functions 1 to get information, 1 to set information

# Create a class called student
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

# Step 2 second iteration

class Student:
    def __init__(self, name, company):
        self.name = name
        self.company = company

    @property # A decorator in python is any callable python object that is used to modify a function or a class
    def Student(self, value):
        print(" This setter method in student data")
        self.__name # __ are used to hide the data

    @Student.setter
    def Student(self, value):
        print(" Calling @student.student method")
        self.__name = value

student_object = Student("Ben", "Sparta Global")

print(f"Student name is {student_object.name}")
print("=" * 34)
print(f"Student works in {student_object.company}")