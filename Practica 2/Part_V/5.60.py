# 60.	Write a NumPy program to get the minimum and maximum value of a given array along the second axis.  
# Expected Output:
# Original array:
# [[0 1]
# [2 3]]
# Maximum value along the second axis:
# [1 3]
# Minimum value along the second axis:
# [0 2]

import numpy as np
x = np.arange(4).reshape((2, 2))

print("\nOriginal array:")
print(x)

print("\nMaximum value along the second axis:")
print(np.amax(x, 1))

print("Minimum value along the second axis:")
print(np.amin(x, 1))