# Rules of blackjack game

# 1. ace is counted as a 1 or 11 dependings on the players choice 
# 2. jack, queen, king are valued as 10
# 3. rest other has the same value as there face value.
# 4. you have to go as close as possible to 21 but going above 21 will cost you to lose.
# 5. the dealer draw's 2 cards for the players and for himself and then betting is done.
# 6. you can request for card extra if you feel your total isn't close to 21 or what you desired.
# 7. if the dealer's card total is less then 16 the dealer has to draw a card.
# 8. on comparing the player closest to the number 21 or equal to 21 wins.
# 9. if the total is equal between an players or the dealer and the player its a draw.    
import os
def clear():
    os.system('cls')

import random

def deal_card():
    """Used to  return the random card from the deck."""
    cards = [11,2,3,4,5,6,7,8,9,10,10,10,10]
    card = random.choice(cards)
    return card

def calculate_score(cards):
    """Takes a list of cards and returns the score calculated from the cards"""
    if sum(cards) == 21 and len(cards) == 2:
        return 0
    if 11 in cards and sum(cards)>21:
        cards.remove(11)    
        cards.append(1)
        
    return sum(cards)

def compare(user_score,computer_score):
    if user_score == computer_score:
        return "Draw"
    elif computer_score == 0:
        return "You Lose,the oppoonent has blackjack!"    
    elif user_score == 0:
        return "You win with a blackjack!"    
    elif user_score > 21:
        return "You lose!"    
    elif computer_score > 21:
        return "You win!"    
    elif user_score > computer_score :
        return "You win!"    
    else :
        return "You lose!"

def play_game():
    user_cards = []
    computer_cards = []
    is_game_over = False
    for _ in range(2):
        user_cards.append(deal_card())
        computer_cards.append(deal_card())

    while not is_game_over:
        
        user_score = calculate_score(user_cards)
        computer_score = calculate_score(computer_cards)
        print(f"Your cards: {user_cards}, current score: {user_score}")
        print(f"Computer's first card: {computer_cards[0]}")

        if user_score == 0 or computer_score == 0 or user_score > 21:
            is_game_over = True
        else:
            user_deal = input("Type 'y' to get another card, type 'n' to pass: ")
            if user_deal == 'y':
                user_cards.append(deal_card())
            else:
                is_game_over = True    

    while computer_score != 0 and computer_score < 17:
        computer_cards.append(deal_card())
        computer_score = calculate_score(computer_cards)

    print(f"Your final hand is: {user_cards} and your score is: {user_score}")
    print(f"Computer's final hand is: {computer_cards} and it's final score is: {computer_score}")
    print(compare(user_score, computer_score))

while input("Do you wanna play blackjack? type 'y' to play and 'n' if not: ")== 'y':
    clear()
    play_game()
