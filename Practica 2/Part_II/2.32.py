# 32.	Write a Python program to find the elements in a given set that are not in another set

set1 = {1,2,3,4,5}
set2 = {4,5,6,7,8}

print("Original sets:")
print(set1)
print(set2)

print("Difference of sn1 and sn2 using difference():")
print(set1.difference(set2))

print("Difference of sn2 and sn1 using difference():")
print(set2.difference(set1))

print("Difference of sn1 and sn2 using - operator:")
print(set1-set2)

print("Difference of sn2 and sn1 using - operator:")
print(set2-set1)