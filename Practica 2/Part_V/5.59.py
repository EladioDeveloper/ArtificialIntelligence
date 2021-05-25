# 59.	Write a Python program to find the maximum and minimum value of a given flattened array. 
# Expected Output:
# Original flattened array:
# [[0 1]
# [2 3]]
# Maximum value of the above flattened array:3
# Minimum value of the above flattened array: 0

import numpy as np
a = np.arange(4).reshape((2,2))

print("Original flattened array:")
print(a)

print("Maximum value of the above flattened array:")
print(np.amax(a))

print("Minimum value of the above flattened array:")
print(np.amin(a))
