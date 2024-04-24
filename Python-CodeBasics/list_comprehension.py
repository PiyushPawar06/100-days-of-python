# # list comprehension helps in tranforming one list to another

# # traditional method
# numbers = [1,2,3,4,5,6,7]
# even = []

# for i in numbers:
#     if i % 2 == 0:
#         even.append(i)
# print(even)        

# # list comprehension
# even = [i for i in numbers if i%2 == 0] # this way the code is more compact.
# print(even)

# sqr_numbers = [i*i for i in numbers]
# print(sqr_numbers)

# # sets are the list which will provide a list with all unique values ie:- no values are repeated and can be unordered

# s = set([1,2,3,4,5,2,3]) # here the values 2 and 3 will be printed only once
# print(s)

# even = {i for i in s if i%2 == 0} # set comprehension
# print(even)

# dictionary comprehension

cities = ["mumbai", "kolkata", "surat"]
states = ["maharashtra", "west bengal", "gujarat"]
z  = zip(cities,states) # this is used to add two or more different lists together.
print(z)
for a in z :
    print(a)

d ={city:state for city,state in zip(cities,states)} # this is dict comprehension
print(d)