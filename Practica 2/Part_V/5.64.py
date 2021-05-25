# 64.	Write a NumPy program to compute the weighted of a given array.  Sample Output:
# Original array:
# [0 1 2 3 4]
# Weighted average of the said array:
# 2.6666666666666665

import numpy as np
x = np.arange(5)

print("\nOriginal array:")
print(x)

weights = np.arange(1, 6)
r1 = np.average(x, weights=weights)
r2 = (x*(weights/weights.sum())).sum()

assert np.allclose(r1, r2)

print("\nWeighted average of the said array:")
print(r1)