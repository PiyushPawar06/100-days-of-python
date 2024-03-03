'''
Treasure Island
Instructions
Make your own "Choose Your Own Adventure" game. Use conditionals such as if, else, 
and elif statements to lay out the logic and the story's path in your program.

To write your code according to my story, you can use this flow chart from draw.io to help you.

However, I think the fun part is writing your own story 😊

🧞‍♂️ 🐊 🧙‍♂️ 🧟 🧚‍♂️ 🧝‍♂️ 🥷 🤖 👽 🙀

That said if you'd like to continue with my example, feel free to use the text snippets below...

Text Snippets from my example
'You're at a crossroad. Where do you want to go? Type "left" or "right"'
'You've come to a lake. There is an island in the middle of the lake. 
Type "wait" to wait for a boat. Type "swim" to swim across.'
"You arrive at the island unharmed. There is a house with 3 doors. 
One red, one yellow and one blue. Which colour do you choose?"
"It's a room full of fire. Game Over."
"You found the treasure! You Win!"
"You enter a room of beasts. Game Over."
"You chose a door that doesn't exist. Game Over."
"You get attacked by an angry trout. Game Over."
"You fell into a hole. Game Over." '''

print("Welcome to  the Treasure Island.\nYour mission is to find the treasure!")
direction =input("Let's start.Do you wanna go left or right? Type: ").lower()

if direction =="left" :
    print("You reached the Blood River.")

    decision = input("Will you wait for the boat or swim? Type: ").lower()
    if decision == "wait":
      print("Boat arrived.\nNow you can take the boat.")

      print("You reached the doors of truth and lies!")       
      final_call = input("Which door do you choose 1,2,3 or 4?Type the following: ")
      if final_call == "1" or final_call == "3" :
            print("You opened the door to bear's cave!You Lose.")
      elif final_call == "2" :
            print("You Went back to start.Start again!")
            start_again = 0
      elif final_call == "4" :
            print("You chose the right door! The treasures' your! \n!!Congratulations!!")  
    else :
        print("You were attacked by cannibal tribe!Game Over.")       
else: 
        print("You fell in to a well of snakes! Game Over.")


    
  


