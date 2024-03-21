def prime_checker(number):
    
    if number % 1 == 0 and number % number == 0:
        print("It's a prime number.")
    else:
        print("It's not a prime number.")    



n = int(input("Please enter a number: "))
prime_checker(number=n)