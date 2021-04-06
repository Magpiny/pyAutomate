"""
@author : Samuel Okoth
@filetype : python OOP
   # Object Oriented Development in python
   # In OOP we have a class and a class in turn has properties and methods
   # Properties describe the appearance while methods describes the functionality
   # A class has objects

         BENEFITS OF OOP
         # Code Reusability (Using objects)
         # Data hiding
         # Extendable code
         # Modular Structure
Checkout example below
"""


class School:
    def __init__(self, name, population, color):
        self.name = name
        self.population = population
        self.color = color

    def learn(self):
        print("We go to school to learn")

    def play(self):
        print("We go to school to play several games")

    def calculate(self):
        print("Please enter your favourite number : ", end=" ")
        namba = int(input())
        print(f"We also calculate squares of {namba} in school...")
        sqr = namba ** 2
        print(f"And the square of {namba} is {sqr}")


school = School("Mulaha Pri School", 896, "Maroon")
print(f"We are from {school.name}", end=" ")
print(f"And our school population is : {school.population}", end=" ")
print(f"And our brand color is {school.color}")

school.play()
school.learn()
school.calculate()


# END OF DISCUSSION

# INHERITANCE IN OOP Python

class AnotherSchool(School):
    pass


school_a = AnotherSchool("Siaya Township Pri School", 1050, "blue")
print(f"{school_a.name} has {school_a.population} students and their brand color is {school_a.color}")
