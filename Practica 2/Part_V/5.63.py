# 63.	Write a NumPy program to compute the median of flattened given array.  Note: First array elements raised to powers from second array
# Expected Output:
# Original array:
# [[ 0 1 2 3 4 5]
# [ 6 7 8 9 10 11]]
# Median of said array:
# 5.5

import numpy as np
x = np.arange(12).reshape((2, 6))

print("\nOriginal array:")
print(x)

r1 =  np.median(x)

print("\nMedian of said array:")
print(r1)