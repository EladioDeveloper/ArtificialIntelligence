numbers = input("Array or tuple: ")

def pickup(list):
    return max(list)

if(numbers[0] == '['):
    parameter = tuple(list(numbers.removeprefix('[').removesuffix(']').split(',')))
    print(pickup(parameter))
elif(numbers[0] == '('):
    parameter = numbers.removeprefix('(').removesuffix(')').split(',')
    print(pickup(parameter))

    




