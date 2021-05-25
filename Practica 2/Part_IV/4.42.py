# 42.	Write a NumPy program to compute the multiplication of two given matrixes.  

import numpy as np
p = [[1, 0], [0, 1]]
q = [[1, 2], [3, 4]]

print("Inputs:")
print(p)
print(q)

result = np.dot(p, q)

print("Result of the said matrix multiplication:")
print(result)
