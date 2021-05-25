# 61.	Write a NumPy program to calculate the difference between the maximum and the minimum values of a given array along the second axis.  
# Expected Output:
# Original array:
# [[ 0 1 2 3 4 5]
# [ 6 7 8 9 10 11]]
# Difference between the maximum and the minimum values of the said array:
# [5 5]

import numpy as np
x = np.arange(12).reshape((2, 6))

print("\nOriginal array:")
print(x)

r1 = np.ptp(x, 1)
r2 = np.amax(x, 1) - np.amin(x, 1)

assert np.allclose(r1, r2)

print("\nDifference between the maximum and the minimum values of the said array:")
print(r1)