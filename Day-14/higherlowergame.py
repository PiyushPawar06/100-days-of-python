from game_data import data
import random
import os
def clear():
    os.system('cls')


def format_data(account):
    '''Takes the account data and returns the printable'''
    account_name = account["name"]
    account_desc = account["description"]
    account_country = account["country"]
    return (f"{account_name}, a/an {account_desc} from {account_country}")

def check_answer(guess,a_followers,b_followers):
    '''Take the users guess and follower counts and returns if  they got it right.'''
    if a_followers > b_followers:
        return guess == "a"
    else:
        return guess == "b"

score = 0
game_should_contiune =True
account_b = random.choice(data)
while game_should_contiune:

    account_a = account_b
    account_b = random.choice(data)
    while account_a == account_b:
        account_b = random.choice(data)

    print(f"Compare A: {format_data(account_a)}.")
    print(f"Against B: {format_data(account_b)}.")

    guess = input("Who has more followers? Type 'A' or 'B': ").lower()
    a_follower_count = account_a["follower_count"]
    b_follower_count = account_b["follower_count"]

    is_correct =check_answer(guess,a_follower_count,b_follower_count)

    clear()

    if is_correct:
        score += 1
        print(f"You are right! Current socre: {score}")
    else:
        game_should_contiune = False
        print(f"Sorry, that's wrong. Final score: {score}")


