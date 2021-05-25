# 62.	Write a NumPy program to compute the 80th percentile for all elements in a given array along the second axis.  Expected Output:
# Original array:
# [1.0, 2.0, 3.0, 4.0]
# Largest integer smaller or equal to the division of the inputs:
# [ 0. 1. 2. 2.]

import numpy as np
x = np.arange(12).reshape((2, 6))

print("\nOriginal array:")
print(x)

r1 = np.percentile(x, 80, 1)

print("\nLargest integer smaller or equal to the division of the inputs:")
print(r1)