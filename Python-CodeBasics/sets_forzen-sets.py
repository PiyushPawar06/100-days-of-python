# basket = {"orange","apple", "mango", "apple", "orange", "apple"} # the set can also be written this way ie:- directly in curly brackets but if you leave the curly brackets empty it will become an dictionary
# print(basket)
# # as set is an unordered list the index method cant be used for example index[0] will given an error
# # another method to write a set is as below
# s = set()
# s.add(1)
# s.add(2)
# s.add(3)
# s.add(4)
# s.add(2)

# print(s)

# # forzen sets are the sets in which you cant modify or change the values of the list 
# numbers = [1,2,3,3,4,5,4,6]
# s = set(numbers)
# s.add(7)
# print (s)

# fs = frozenset(numbers) # if we try n add any number it with throw an error
# print(fs) 

# you can perfrom set opreations too!
a ={1,2,3,4}
b = {3,4,5,6}

print(a | b ) # a union b
print (a & b) # a intersection b
print(a - b) # difference between two sets
print(a < b) # to check whether a is subset of b
 