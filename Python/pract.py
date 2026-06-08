class Student:

    school = "ABC School"

    @classmethod
    def display_school(cls):
        print(f"School Name: {cls.school}")


Student.display_school()


class Calculator:

    @staticmethod
    def add(a, b):
        print(a + b)


Calculator.add(10, 20)


class Student:

    school = "ABC School"

    def __init__(self, name):
        self.name = name

    # Instance Method
    def display_student(self):
        print(self.name)

    # Class Method
    @classmethod
    def display_school(cls):
        print(cls.school)

    # Static Method
    @staticmethod
    def add(a, b):
        print(a + b)


stud = Student("Azar")

stud.display_student()      # self
Student.display_school()    # cls
Student.add(10, 20)         # static


class Calculator:

    def add(self, *args):
        print(sum(args))


obj = Calculator()

obj.add(10, 20)
obj.add(10, 20, 30)
obj.add(10, 20, 30, 40)


over riding:
    

class Animal:
    def sound(self):
        print("Animal Sound")

class Dog(Animal):
    def sound(self):
        print("Dog Barks")

obj = Dog()
obj.sound()


abstract:
from abc import ABC, abstractmethod

class Vehicle(ABC):

    @abstractmethod
    def start(self):
        pass

class Bike(Vehicle):

    def start(self):
        print("Bike Started")

b = Bike()
b.start()


class Employee:

    def __init__(self, name):
        self.name = name


class Developer(Employee):

    def __init__(self, name, language):
        super().__init__(name)
        self.language = language

    def display(self):
        print(f"Name : {self.name}")
        print(f"Language : {self.language}")


obj = Developer("Azar", "Python")
obj.display()





class Test:
    school_name="MM"
    def student(self,name):
        print(name)
    @classmethod
    def display_school(cls):
        print(cls.school_name)
        
    @staticmethod
    def total_mark(a,b):
        print(a+b)
        
t=Test()
t.display_school()
t.student("tamil")
t.total_mark(4,5)


from abc import ABC,abstractmethod
class Vechicle(ABC):
    def __init__(self,name,brand):
        self.name=name
        self.brand=brand
    
    @abstractmethod
    def display():
        pass
    
class Car(Vechicle):
        def __init__(self,name,brand):
            super().__init__(name,brand)
        def display(self):
            print(self.name,self.brand)
            
c=Car("name","brand")
c.display()

    
 from abc import ABC,abstractmethod
class Vehicle(ABC):
    @abstractmethod
    def display(self):
        pass
    
class Car(Vehicle):
    def display(self):
        print("I am car")
        
c=Car()
c.display()


from abc import ABC ,abstractmethod
class Vehicle(ABC):
    def __init__(self,brand,color):
        self.brand=brand
        self.color=color
    @abstractmethod
    def display(self):
        pass
    
v=Vehicle("m",1)
v.display
    
class Car(Vehicle):
    def __init__(self, brand, color):
        super().__init__(brand, color)
        
    def display(self):
        print(self.brand,self.color)
        
c= Car("Maruthi","red")
c.display()        
c.display()    


class Vehicle:
    def __init__(self,brand,color):
        self.brand=brand
        self.color=color
  
    def display(self):
        print(self.brand,self.color)
    
class Car(Vehicle):
    def __init__(self, brand, color,type):
        super().__init__(brand, color)
        self.type=type
        
    def display(self):
        super().display()
        print(self.type)
        
c= Car("Maruthi","red","Gas")
c.display()   

class Flyer:
    def fly(self):
        return(" I Fly")
class Swimer:
    def swim(self):
        return("i swim")
        
class Duck(Flyer,Swimer):
    pass

d=Duck()
print(d.fly())
print(d.swim())


class A():
    def __init__(self):
        print("Class A")
        
    
class B(A):
    def __init__(self):
        super().__init__()
        print("class B")
        
class C(A):
    def __init__(self):
        super().__init__()
        print("C")
        
class D (B,C):
    def __init__(self):
        super().__init__()
        print("d")

d=D()
print(D.__mro__)


class Base:
    def __init__(self):
        print("Base init")

class Left(Base):
    def __init__(self):
        super().__init__()
        print("Left init")

class Right(Base):
    def __init__(self):
        super().__init__()
        print("Right init")

class Child(Left, Right):
    def __init__(self):
        super().__init__()
        print("Child init")

# Instantiating Child triggers the entire MRO chain
c = Child()   
       