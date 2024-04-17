"""
trees = 1

def increase_trees():
    trees = 2
    print(f"The no. of trees inside the funtion are: {trees}")

increase_trees()    
print(f"The no. of trees outside the funtion are:{trees}")
"""
# Local scope : you can call the statements that are defined the funtion within the same funtion. else it will throw an error.

# def potion():
#     potion_strength = 2
#     print(potion_strength)

# potion()
# print(potion_strength) // here you will get an error as your are calling a local variable outside of its scope.

# Globle scope: the statements defined at the top outside the funtion and can be called through out the code anywhere are called globle funtion.
'''
player_health = 10
def potion():
    potion_strength = 2
    print(player_health)

potion()
'''
# There are no block scope in python therefore the blocks where there is a use of indentation and colon cannot be counted as local scope unless there are defined in a funtion
'''
eneimes = ["skeleton", "zombies", "aliens"]
def create_eneimes():

    game_level = 3
    if game_level < 5:
        new_enemy = eneimes[0]
'''
# print(new_enemy) // here if we try and print this statement it will give a name error as now the if statement block is inside a funtion called create_eneimes and we are trying to print the new_enemy outside the funtion

# Modifying the globle scope

person = 1

def total_people():
    global person # // here the keyword global is used to call the globle variable inside the local variable. 
    person += 1
    print(person)

total_people()










