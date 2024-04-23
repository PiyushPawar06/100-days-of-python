# file = open("D://100-days-of-python//Python-CodeBasics//HelloWorld.txt", "w") // 'w' is to write the text in the file but whenever you write it will overwrite the pervious written text in the file.
# file.write("Hello World!")
# file.close() // this is used to close the process as the allocated memory will be freed.

# file = open("D://100-days-of-python//Python-CodeBasics//HelloWorld.txt", "a") # here 'a' is used to append the text in the file where it will append the new text without overwritting the pervious text.
# file.write("Hello World!")
# file.close()

file = open("D://100-days-of-python//Python-CodeBasics//HelloWorld.txt", "r") # 'r' is used to read the contents of the file.
# print(file.read())
for line in file: # this will read line by line.
    # print(line) 
    words = line.split(' ') # this will give you all the words in the file spreately as a string.
    print(str(words))
    print(len(words)) # to know the number of words in a row i the file.
file.close()

with open("D://100-days-of-python//Python-CodeBasics//HelloWorld.txt", "w") as file: # this will help you to close the file if you forget to use the close statement.
    file.write("Hello World!")