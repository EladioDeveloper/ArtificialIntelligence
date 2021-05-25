# 7. Convert the tuples to lists and in the point 6 and calculate the average.

tup = [(1, 2), (3, 4), (5, 6)]
  
result = []
  
for t in tup:
    for x in t:
        result.append(x)
  
print(result)