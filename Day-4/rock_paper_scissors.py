'''
Make a rock, paper, scissors game.

Start the game by asking the player:

"What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors."

From there you will need to figure out:

How you will store the user's input.
How you will generate a random choice for the computer.
How you will compare the user's and the computer's choice to determine the winner (or a draw).
And also how you will give feedback to the player.'''
import random



rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
images = [rock,paper,scissors]
computer_choice = random.randint(0,2)

my_choice = int(input("What would you choose? Type 0 for rock,1 for paper or 2 for scissors: "))

if my_choice > 2 or my_choice < 0:
    print("Your input is invalid,\nyou lose!")
else:
    print(images[my_choice])
    print(f"Computer chose:")
    print(images[computer_choice])  
 
    if computer_choice == 0 and my_choice == 2:
        print("You lose!")
            
    elif computer_choice == 2 and my_choice == 0:
        print("You win!")
    elif computer_choice > my_choice:
        print("You lose!")   
    elif my_choice > computer_choice :
        print("You win!")    
    elif my_choice == computer_choice:
        print("Draw!")    
        
    else :
        print()

