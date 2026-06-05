1. Class & Object
2. Constructor (__init__)
3. Instance Variables
4. Instance Method
5. Types of Methods
   - Instance Method
   - Class Method
   - Static Method
6. Encapsulation
7. Inheritance
8. Polymorphism
9. Abstraction

# class Classname:
#     variable
#     def function_name:
#         pass
    
    
# ogj= Classname()



class Student:
    def __init__(self,name,address):
        self.name=name
        self.addr=address
     
    @staticmethod   
    def display_info(self):
        print(f" Name = {self.name} Address = {self.addr}")
    
stud=Student("Azar","Chennai")
stud.display_info()


# 3Types:
# 1.class - cls
# 2.Instance - self
# 3.static - @static

# Encapsulation
# _name => Protected
# __password => Private

class Customer:
    def __init__(self,fname,username,password):
        self.fname=fname
        self._username=username  #protected
        self.__password=password #Private
        
    def display_info(self):
        print(f"Firstname {self.fname} , Username {self._username} password {self.__password}")
    
cust=Customer("Tamilzhisai",'tamil',"tamil@123")
cust.display_info()
print(cust._username)
print(cust._Customer__password)


# cust._classname__variableName

#Inheritance
# 1. single Inheritance
# 2. Multilevel Inheritance
# 3. Multiple Inheritance  (multiple Parent)
# 4. Hieriachical Inheritance (Multiple Child, 1 Parent)

class Parent:
    def display(self):
        print("I am Parent Class")
        
class Child(Parent):
    def childfunc(self):
        print("I am Child Class")
        
class Gchild(Child):
    def grandfunc(self):
        print("I am GrandChild")
        
# prt=Parent()   
# prt.display()

# ch = Child()
# ch.display()
# ch.childfunc()

gd=Gchild()
gd.display()
gd.childfunc()
gd.grandfunc()


class Parent:
    def display(self):
        print("I am Parent Class")
        
class Child():
    def childfunc(self):
        print("I am Child Class")
        
class Gchild(Parent,Child):
    def grandfunc(self):
        print("I am GrandChild")
        
gd=Gchild()
gd.grandfunc()
gd.childfunc()
gd.display()









