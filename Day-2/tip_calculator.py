#If the bill was $150.00, split between 5 people, with 12% tip. 

#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60

#Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪

#Write your code below this line 👇

print("Welcome to the tip calculator!")
total_bill = float(input(f"What is your total bill? $"))
tip = int(input(f"How much percent tip you wanna add?10,12,15: "))
total_tip = float(total_bill*(tip/100))
new_total_bill = total_tip + total_bill
people = int(input(f"Total number of people? "))
contri = round(new_total_bill/people,2)
print(f"The contri per person is:{contri}")
