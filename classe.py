class Dog():
    """ A simple attempt to model a dog"""
    def __init__(self, name, age):
        """ Initialize age and name attributes. """
        self.name = name
        self.age = age
        
    def sit(self):
        """ Simulate a dog sitting in response to a command """
        print(f"{self.name.title()} is now sitting.")
        
    def roll_over(self):
        """Simulate rolling over in response to a command"""
        print(f"{self.name.title()} rolled over!")
        
    def bark(self):
        """ Simulate barking in response to a command """
        print(f"{self.name.title()} is barking!")
        print("WOF")
        
    def walk(self):
        """ Simulate barking in response to a command """
        print(f"{self.name.title()} is walking")
      

class Car():
    """ An attempt  to represent a car"""
    def __init__(self, make, model, year):        
        """ Initialize attributes to describe a car"""
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0
    
    def get_descriptive_name(self):
        """ Return a neatly formatted descriptive name"""
        long_name = str(self.year) + " " + self.make + " " + self.model
        return long_name.title()
        
    def read_odometer(self):
         """ print a statement showing the car's mileage"""
         print(f"This car has {self.odometer_reading} miles on it.")
         
    def update_odometer(self, mileage):
        """ 
        set the odometer reading to the given value 
        Reject the change if it tries to roll back the odometer
        """
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't roll back an odometer")
            
    def increment_odometer(self, miles):
         """ 
         Add the given amount to the odometer reading
         Reject the change if it tries to roll back the odometet
         """
         if miles > 0:
             self.odometer_reading += miles
         else:
             print("You can't roll back an odometer")  
               
my_car = Car("Benz", "setback", 2030)     

  

class Student:
    """ 
    An attempt to collect and display students information
    """
    def __init__(self, first_name, middle_name, surname, course, school, level=100):
        self.first_name = first_name
        self.middle_name = middle_name
        self.surname = surname
        self.course = course
        self.level = level
        self.school = school
        
    def get_full_name(self):
        """ Return a neatly formatted name"""
        full_name = self.first_name + " " + self.middle_name + " " + self.surname
        return full_name.title()
        
    def introduce(self):
        """ Display a brief introduction about a student"""
        fullname = self.get_full_name()
        print(f"Hello, my name is {fullname}. from {self.school}, I am studying {self.course}, I am in {self.level} level.")
        
    def promote(self, increment=100):
        """ Increment a students level"""
        self.level += increment                
        
    def change_course(self, new_course):
        """ Change the. course value to this value"""
        self.course = new_course
        
class Battery:
    """A simple attempt to model a battery for an Electric car"""

    def __init__(self, battery_size=70):
        self.battery_size = battery_size

    def describe_battery(self):
        print(f"This car has a {self.battery_size}-KWH battery")

    def get_range(self):
        if self.battery_size == 70:
            battery_range = 240
        elif self.battery_size == 85:
            battery_range = 270
        else:
            battery_range = 0

        print(f"This car can go approximately {battery_range} miles on a full charge")

    def charge_battery(self, charge):
        if charge < self.battery_size:
            print("You can't decrease the battery size.")
        else:
            self.battery_size = chargeA
            
class ElectricCar(Car):
        """
        Represent aspects of a car, specific to electric vehicles.       
        """   
        def __init__(self, make, model, year):
            """
             Initialize attributes of the parent class
             Then initialize attributes specific to the child class
             """
            super().__init__(make, model, year)
            self.battery = Battery()
            
        
        
my_tesla = ElectricCar("Tesla", "model S", 2016)
print(my_tesla.get_descriptive_name())

my_tesla.battery.describe_battery()
my_tesla.battery.charge_battery(80)
my_tesla.battery.get_range()
