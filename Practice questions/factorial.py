
while True:
    user_number = int(input("Please enter a number: ")) 
    if user_number < 0:
        print("Invalid input")
    elif user_number == 0:
        print(f"The factorial of {user_number} is 1")    
    else:
        break    
fact = 1
for number in range(1,user_number+1):
    fact *= number
    print(fact)    