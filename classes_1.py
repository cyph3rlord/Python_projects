class Animal:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        
    def walk(self):
        print("walking...")

class Dog(Animal):
    
    def bark(self):
        print("WOF!")
        
class Vehicles:
    def __init__(self, name, color, price):
        self.name = name
        self.color = color
        self.price = price
        
    def start(self):
        print("Chinhinhin Vuuum")
        
class Cars(Vehicles):
        def park(self):
            print("Parked")    
                
class Student:
    
    def __init__ (self, name, id_number, age):
        self.name = name
        self.id_number = id_number
        self.age = age
        
    def greet_student(self, greetings):
        print(f"Hello, {self.name}. {greetings}")    
        