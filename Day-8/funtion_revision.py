# Basic funtion

def greet():
    print("Hello Guys")
    print("How are you doing?")
    print("What's New?")

greet()
# funtion with a variable the allows input

def greet_with_name(name): # there the name is addressed as a parameter
    print(f"Hello {name}")
    print(f"{name} what's your last name?")

greet_with_name("Aryan") #this dosen't requrie a input line because we directly assign the 
                         #value to the variable here. 
# in above line Aryan is addressed as argument,which is passed in the parameter(which is name)

# funtion with multiple input

def greet_with(name, location):
    print(f"Hello {name}!")
    print(f"Are you from {location}?")

greet_with("Aryan", "Pune")    # this is  positional argument

# keywords argument

def numbers(a,b,c):
    print(f"{a}")

numbers(a=1,b=2,c=3) #here we can intentionally assign the parameter the argument we want so
                     #so that even if we rearrange the places of the it the arguments wont change

greet_with(name = "Vishwa", location = "Pune")  
