#1.	Write a Python program to count the number of characters (character frequency) in a string. Sample String : google.com'. 
# Expected Result : {'g': 2, 'o': 3, 'l': 1, 'e': 1, '.': 1, 'c': 1, 'm': 1}

word = input("Write a word: ")
dictionary = {}
for x in word:
    keys = dict.keys()
    if x in keys:
        dictionary[x] += 1
    else:
        dictionary[x] = 1

print(dict)