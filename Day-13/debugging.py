############DEBUGGING#####################

# # Describe Problem
# def my_function():
#   for i in range(1, 20): //here the range should be till 21 in order for code to run. 
#     if i == 20:
#       print("You got it")
# my_function()

# # Reproduce the Bug
# from random import randint
# dice_imgs = ["❶", "❷", "❸", "❹", "❺", "❻"]
# dice_num = randint(1, 6) // here the range should be from 0 to 5 as randint includes starting and ending values too. also the list at line 12 starts its count from 0 therefore we have to give the range of (0,5) in randint funtion.
# print(dice_imgs[dice_num])

# # Play Computer
# year = int(input("What's your year of birth?"))
# if year > 1980 and year < 1994: // here the year 1994 isnt included and neither it is included in line 20 therefore the both if and elif statements becomes false. and nothing will be printed. you have to change the condition either at line 18 or 20 by adding an equal to sign for 1994. 
#   print("You are a millenial.")
# elif year > 1994:
#   print("You are a Gen Z.")

# # Fix the Errors
# age = input("How old are you?") // convert the input to int as the output of this given input statement will be an string.
# if age > 18:
# print("You can drive at age {age}.") // give an Indentation,also add and f string. 

# #Print is Your Friend
# pages = 0
# word_per_page = 0
# pages = int(input("Number of pages: "))
# word_per_page == int(input("Number of words per page: ")) // if unable to understand the error try and use print statements to narrow down the problem. in this example you can print the values of pages inputed and word_per_page inputed by the user. that gives us word_per_page as 0 irrespective of the input given this is because on line 32 we have given double equal to sign which asks us where the input is equal to the inital assigned value of word_per_page rather then asigning the input value which is done by single equal to sign.
# total_words = pages * word_per_page
# print(total_words)

#Use a Debugger
def mutate(a_list):
  b_list = []
  for item in a_list:
    new_item = item * 2
  b_list.append(new_item)
  print(b_list)

mutate([1,2,3,5,8,13])