import random
#Random_module
random_int = random.randint(1,10)
print(random_int)

random_float = random.random() * 5

print(random_float)
love_score = random.randint(1,100)
print(f"Your love score is: {love_score} ")

#lists

states_of_india = ["Maharashtra","Goa","MP","UP","AP"]
states_of_india[2] = "Madhya Pradesh" #this is used to change the data in the list
states_of_india.append("Kerla")
print(states_of_india[2])

print(states_of_india[-1])

#nested lists
fruits=["Strawberies","Apples","Grapes","Peaches"]
vegetables = ["Spinach","Kale","Tomato"]
most_pesticides = [fruits,vegetables]
print(most_pesticides[0][1])
print(most_pesticides[1][1])