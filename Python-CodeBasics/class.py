# a class is a group in which there are properties and methods for example human is a class and name, gender are its properties and the way that human speaks, walks can be called as its method.

# Object is the set of different humans. for example John Cena is a human with different properties such as unique name as john cena and gender is male and different methods as he speaks english where as Alia Bhatt is another human with different properties such as a unique name as alia bhatt and gender is female and different methods as she speaks hindi.

class Human:
    def __init__(self, n, o): # this a property. here the self means the self class. and the __init__ is used to initiate that self funtion and n and o are parameters
        self.name = n # here 'name' is the property
        self.occupation = o # here 'occupation' is the property

    def do_work(self): # this is a method 
        if self.occupation == "Boxer":
            print(f"{self.name} is an UFC Boxer")   
        elif self.occupation == "Actor":
            print(f"{self.name} shoots flims.")    

    def says(self):
        print(f"{self.name} says How are you?")        

Conor = Human("Conor", "Boxer") # This is an object. here you dont need to pass the self as it is predefined only pass the variables.        
Conor.do_work()
Conor.says()

Ranbir = Human("Ranbir", "Actor")
Ranbir.do_work()
Ranbir.says()