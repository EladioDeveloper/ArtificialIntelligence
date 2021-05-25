# 1.	Write a Python program to count the number of characters (character frequency) in a string. Sample String : google.com'. Expected Result : {'g': 2, 'o': 3, 'l': 1, 'e': 1, '.': 1, 'c': 1, 'm': 1}

def character_frequency(input):
    dictionary = {}
    for n in input:
        keys = dictionary.keys()
        if n in keys:
            dictionary[n] += 1
        else:
            dictionary[n] = 1
    return dictionary
print(character_frequency('google.com'))