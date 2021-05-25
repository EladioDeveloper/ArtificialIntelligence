#40.	  Write a Python program to solve FACTORIAL sequence FROM N as non-negative integer using recursion

def factorial(n):
  if n <= 1:
    return 1
  else:
    return n * (factorial(n - 1))
    
print(factorial(5))