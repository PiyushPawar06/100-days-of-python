import os
def clear():
    os.system('cls')

from random import randint
EASY_LEVEL = 10
HARD_LEVEL = 5
def check_the_guess(guess,the_number, turns):
    if guess>the_number:
        print("Too high !!!")
        return turns - 1
    elif guess<the_number:
        print("Too low !!!") 
        return turns - 1

    else:
        print(f"That's the right guess! The answer is {the_number}") 
        return 


def difficulty():
    difficulty_level = input("Please choose the level of difficulty 'easy' or 'hard' : ")
    if difficulty_level == "easy":
        return EASY_LEVEL
    elif difficulty_level == "hard":
        return HARD_LEVEL    

def guessing_game():
    the_number = randint(1,100)

    print("Welcome to the guessing game! ")
    print("The PC will choose a number from 1 to 100 and you Guess the number")

    turns = difficulty()
    

    guess = 0
    while guess != the_number:
        print(f"You have {turns} attempts left to guess the number!")
        guess = int(input("Guess the number: "))

        turns = check_the_guess(guess, the_number, turns)
        if turns == 0:
            print("Your are out of attempts,You lose!")
            return

         
  

guessing_game()  
restart = input("Do you wanna restart the game? type 'yes' or 'no': ")      
if restart == 'yes':
    clear()   
    guessing_game()
else:
    print("Thank you! Have a good day")    