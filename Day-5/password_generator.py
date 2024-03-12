import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q',
           'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 
           'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W',
           'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
print("Welcome to  the Password Generator!")
print("How many number of letters/symbols/numers?\n")
letter_input = int(input())
# print ("How many numbers would you like in your Password?\n")
# number_input = int(input())
# print("How many Special Charaters would you like in your Password?\n")
# symbol_input = int(input())
random_choice_letter=[]
for i in range(letter_input):
    random_choice_letter.append(random.choice(letters))
    random_choice_letter.append(random.choice(numbers))
    random_choice_letter.append(random.choice(symbols))

random.shuffle(random_choice_letter)
print(''.join(random_choice_letter))

