def sum(a, b, c):
    if a == b or b == c or a == c:
        sum = 0
    else:
        sum = a + b + c
    return sum
number1 = int(input("Enter the #1: "))
number2 = int(input("Enter the #2: "))
number3 = int(input("Enter the #3: "))

print(sum(number1, number2, number3))
