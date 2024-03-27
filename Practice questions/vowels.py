str1 = input("Please enter a word/sentence: ")
vowel = "aeiouAEIOU"
count = 0
for n in str1 :
    if n in vowel:
        count += 1
print(f"total number of vowels is/are: {count}") 
