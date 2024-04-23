book = {}
book['Aryan'] = {
    'name' : 'Aryan',
    'Address' : 'Icchalkaranji',
    'Phone_number':1234567890
}

book['Vishwa'] = {
    'name' : 'Vishwa',
    'Address' : 'Kadegaon',
    'Phone_number':2345678901
}
import json

s = json.dumps(book) #this will dump the dictonary into a string and that string is a json format,that's why dump with a 's'.
print(s)
with open("D://100-days-of-python//Python-CodeBasics//book.txt", "w") as f:
    f.write(s) # here we are writing the dictionary book as a readable file using .write(varible in which the dictionary is dumped) and it will create a book.txt file in  the provided folder path.
f = open("D://100-days-of-python//Python-CodeBasics//book.txt", "r") 
b = f.read() # to read the json file.
print(b)

book_1 = json.loads(b) # this will give the output as a json file where as the above will give the output as a string.
print(book_1)

for person in book:
    print(book[person])
