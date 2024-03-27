#  Factors print karayche number che
#  Ata samaj 6 num ahe
#  Tyache factors kay yenar 1, 2 ,3, ani 6
#  He print zhala pahije
#  Bgh kasa karaych
while True:
    user_number = int(input("Please enter a number: "))
    if user_number == 1 or user_number <= 0 :
        print("Invalid input!")
    else:       
        break 
facotrs_list = []
for number in range(1,user_number+1):
    if user_number % number == 0 :
        facotrs_list.append(number)
print(facotrs_list)

if len(facotrs_list) == 2:
    print(f"The {user_number} is a prime number")
else :
    print(f"The {user_number} is composite number.")    