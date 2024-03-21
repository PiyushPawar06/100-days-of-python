# a dictionary in python is used to group together the piece of info and tag the related info 
# the syntax is {Key: Value}
programming_dictionary = {
"bug":"An error in the program that prevents the program from running as excepted.", "funtion":"A piece of code that can be called easily over and over again"
}

# this is used to retrive the value of the mentioned key
print(programming_dictionary["bug"])

# adding a new key
programming_dictionary["loop"] = "The action of doing something over and over again"
print(programming_dictionary["loop"])

# wipe an existing dictionary 
programming_dictionary = {} 
print(programming_dictionary)

# editing an item in the dictionary 
programming_dictionary["bug"] = "A moth in your computer."
print(programming_dictionary)

# loop through a dictionary
for key in programming_dictionary:
    print(key)
    print(programming_dictionary[key])

# Nesting is used to nest list and dictionary in one another
capitals = {
    "France" : "Paris",
    "Germany" : "Berlin"
}

# nesting a list in dictionary
travel_log = {
    "India" :{"cities_visited" : ["Pune","Mumbai","Delhi"],"total_visits": 12},
    "Japan" : ["Tokyo", "Kyoto", "Okasa"]
}

# list in a list
list_in_list = ["butter","chicken",["with skin"]]

# dictionary in dictionary
cities_visited = {
    ""
}

# dictionary in  a list
travel_log = [
    {
    "country" :"India",
    "cities_visited" : ["Pune","Mumbai","Delhi"],
    "total_visits": 12
    },

    {
    "country" :"Japan",
    "cities_visited" : ["Tokyo", "Kyoto", "Okasa"] ,
    "total_vists":5
    }
]
s = {
    "a" : 9,
    "b" : 8,

}

f ={
    "a" : 9 , 
    "b" : 8 ,
    "c" : 7
}
