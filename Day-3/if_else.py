
#Rollercoaster ride entry requriement.
#if you are above 120cm tall you can enjoy the ride.  

print("Welcome to the rollercoaster ride!!!")

'''height = int(input("Please enter your height in cm: "))
age = int(input("Please enter your age: "))
if height >= 120 and age >=18 : 
    print("You can ride the Roller-Coaster!")
    #nested if-else loop
  #  age = int(input("Please enter your age: "))
    # if age <= 18 :
    #     print("Please pay $7.")
    # else:
    #     print("Please pay $12.")    sg
else:
    print("Sorry you can't ride the Roller-coaster.")'''

#elif in if-else statements 
'''
height = int(input("Please enter your height in cm: "))

if height >= 120 :
    print("You can ride the roller coaster!!!") 
    age = int(input("Please enter your age: "))
    if age <=5 :
        print("Sorry you can ride the roller coaster.")
    elif age <= 12:
        print("Please pay $5.")
    elif age<=18 :
        print("Please pay $7.")    
    else :
        print("Please pay $12.")    
  
else : 
    print("Sorry you can't ride the roller coaster.") 
'''
#Multiple if statements
height = int(input("Please enter your height in cm: "))
bill = 0
if height > 120:
    print("You can ride the roller coaster!!!")
    age = int(input("Please enter your age: "))
    if age < 5:
        print("Sorry you can't ride the roller coaster.")
    elif age <= 12 :
        bill = 5
        print("Your ticket price is $5.")    
    elif age <= 18:
        bill = 7
        print("Your ticket price is $7.") 
   #logical opreators.
    elif  age >= 45 and age <= 55:
        print("Today the ride is free for people between the age 45-50.Enjoy!")   
    else :
        bill = 12
        print("Your ticket price is $12.") 
    want_photos = input("Would you like a photo on the roller coaster? Y or N: ")       
#mutliple if statement is used here.
    if  want_photos =="Y" :
        bill +=3
    print(f"Your total bill is ${bill}.") 
else:
    print("Sorry, you can't ride the roller coaster.")    

    