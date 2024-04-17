# def prime_checker(number):

n = int(input("Please enter a number: "))


prime_num = []
for num in range(2,n + 1):
    # print(i)
    if n % num == 0 :
        prime_num.append(num)
print(prime_num)        
      
    

    

# prime_checker(number=n)