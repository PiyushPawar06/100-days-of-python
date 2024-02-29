#String

print("Hello"[4])
print("123" + "345")

#Integer 

print(123+34)

#float 

print(123.45)
print(70 + float("100.75"))

#boolean

True 
False

#type_castings

num_char = len(input("What is your name?"))
new_num_char = str(num_char)

print("Your name has " + new_num_char +" charaters." )
print(str(70)+str(100)) 

#Mathamatical operations
print(7+3)
print(7-3)
print(7*3)
print(7/3)
print(7**3)
print(7*7+10-7**8/2)
print(round(8/3))
print(round(8/3,2))
print(7//2)

#Number manipulation
result = 4/2
result +=2
print(result) 

#f-string
name = input()
num = 10
print(f"have a good day {name},you are a {num}")