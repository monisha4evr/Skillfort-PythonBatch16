class Fruit:

    fruit1 = "Apple"
    fruit2 = "Mango"
    fruit3 = "Orange"

    @classmethod
    def display_fruits(cls):
        print("Fruit 1 :", cls.fruit1)
        print("Fruit 2 :", cls.fruit2)
        print("Fruit 3 :", cls.fruit3)


Fruit.display_fruits()
# Output:
    
# Fruit 1 : Apple
# Fruit 2 : Mango
# Fruit 3 : Orange


class Student:

    def __init__(self, name):
        self.name = name

    @staticmethod
    def total_mark(m1, m2, m3):
        return m1 + m2 + m3

    def display(self, total):
        print("Student Name :", self.name)
        print("Total Mark :", total)


s1 = Student("Monisha")

total = Student.total_mark(80, 90, 85)

s1.display(total)

# Output:
    
# Student Name : Monisha
# Total Mark : 255

class Student:

    def __init__(self, name, course):
        self.name = name
        self.course = course

    def display(self):
        print("Name :", self.name)
        print("Course :", self.course)


s1 = Student("Monisha", "Python Full Stack")
s1.display()
# Output
# Name : Monisha
# Course : Python Full Stack