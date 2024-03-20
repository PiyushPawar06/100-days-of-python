
# from random_word import RandomWords
# r = RandomWords()
# r.get_random_word()

#todo-1 - Randomly choose a word from the word_list and assign it to a
#         variable called chosen_word.

#todo-2 - Ask the user to guess a letter and assign their answer to a variable called guess. 
#         Make guess lowercase.

#todo-3 - Check if the letter the user guessed (guess) is one of the letters in the
#         chosen_word.
import random
import hangman_art
import hangman_words


chosen_word = random.choice(hangman_words.word_list).lower()
lives = 6
print(hangman_art.logo)

print(f"This might be the answer: {chosen_word}")
display = []
for letter in chosen_word:
    display += "_"
print(display)
game_ended = False
while not game_ended:
    guess =input("Guess a letter:").lower()

    if guess in display:
        print(f"You have already guessed{guess}")
    for position in range(len(chosen_word)):
        letter = chosen_word[position]
        if letter == guess:  
            display[position] = letter
    if guess not in chosen_word:
        print(f"The guessed letter {guess} isn't in the word.You lose a life.")
        lives -= 1
        if lives == 0:
            game_ended = True
            print("You Lost")        
    print(display)          

    if "_" not in display:
        game_ended = True
        print("You Won")
    print(hangman_art.stages[lives])    

       
        
#todo-1: - Create an empty List called display.
#For each letter in the chosen_word, add a "_" to 'display'.
#So if the chosen_word was "apple", display should be ["_", "_", "_", "_", "_"] with 5 "_" representing each letter to guess.



#todo-2: - Loop through each position in the chosen_word;
#If the letter at that position matches 'guess' then reveal that letter in the display at that position.
#e.g. If the user guessed "p" and the chosen word was "apple", then display should be ["_", "p", "p", "_", "_"].


#todo-3: - Print 'display' and you should see the guessed letter in the correct position and every other letter replace with "_".
#Hint - Don't worry about getting the user to guess the next letter. We'll tackle that in step 3.
