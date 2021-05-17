def differents(numbers):
  if len(numbers) == len(set(numbers)):
    return "There are differents"
  else:
    return "There are not differents"

print(differents([1,2,3,4,5,6]))
print(differents([3,2,1,6,3,4]))

