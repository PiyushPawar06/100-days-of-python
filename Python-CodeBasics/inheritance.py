# Inheritance increases code reusablity . 
# It also makes the code extensibe as you can extended the properties and methods 
# It gives a structure to the code and makes it more readable




class Vehicle: # parent class
    def general_use(self):
        print("Transportation")

class Car(Vehicle): # child calss
    def __init__(self) :
        print("I'm Car")
        self.wheels = 4
        self.roof = True

    def specific_use(self):
        print("Is used for vacation")    

class Bike(Vehicle): #second child class
    def __init__(self) :
        self.general_use() # you can also call the properties of parent class within the child class.
        print("I'm Bike")
        self.wheels = 2
        self.roof = False

    def specific_use(self):
        print("Long Ride")    
        
c = Car()     
c.general_use()   # even though there isnt any method or property defined in class car the genral_use of car can be spcified as it is defined in parent class and the child class inherit the properties and methods of parent class.
c.specific_use()

b = Bike()

b.specific_use()

print(isinstance(c,Car)) # tells whether 'c' is an instance of class Car or not. will print true.

print(issubclass(Car,Vehicle)) # tells whether Car is a subclass of Vehicle or not.