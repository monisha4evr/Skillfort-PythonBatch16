class Calculation:
    def add(self,a,b,c=None):
        print(a+b+c)
        
calc=Calculation()
calc.add(1,2,3)
        
from abc import ABC,abstractmethod
class Vehicle(ABC):
    def __init__(self,name,brand):
        self.name=name
        self.brand=brand
        
    @abstractmethod
    def display(self):
        pass
    
class Car(Vehicle):
    def __init__(self, name, brand):
        super().__init__(name, brand)
        
    def vehicle_info(self):
        print(self.name,self.brand)
        
    def display(self):
        print("CAR")
c=Car("MAruthi 800","Maruthi")
c.display()
c.vehicle_info()


class Vehicle:
    def __init__(self,brand,color):
        self.brand=brand
        self.color=color
        
    def display_info(self):
        print(f" Brand = {self.brand}, Color={self.color}")
        
class Car(Vehicle):
    def __init__(self,brand, color,fuel_type):
        super().__init__(brand, color)
        self.fuel_type=fuel_type
        
    def display(self):
        super().display_info()
        print(f"Fuel Type{self.fuel_type}")
        
c=Car("Maruthi","Red","Gas")
c.display()

