'''
for i in range(5):
    for j in range(0,i+1):
        print("* ",end='')
    print("\r")
'''
def prime_checker(number):
  is_prime = True
  for i in range(2, number):
    if number % i == 0:
      is_prime = False
  if is_prime:
    print("It's a prime number.")
  else:
    print("It's not a prime number.")
    
# Your code above this line 👆
n = int(input()) # Check this number
prime_checker(number=n)