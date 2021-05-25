# 44.	Write a NumPy program to compute the cross product of two given vectors.

import numpy as np
p = [[1, 0], [0, 1]]
q = [[1, 2], [3, 4]]

print("Inputs:")
print(p)
print(q)

result1 = np.cross(p, q)
result2 = np.cross(q, p)

print("cross product of the said two vectors(p, q):")
print(result1)

print("cross product of the said two vectors(q, p):")
print(result2)  