def LCM(x, y):
   if x > y:
       z = x
   else:
       z = y

   while(True):
       if((z % x == 0) and (z % y == 0)):
           lcm = z
           break
       z += 1

   return lcm

inferior_limit = int(input("Enter the inferior limit: "))
superior_limit = int(input("Enter the superior limit: "))
print("LCM = ", LCM(inferior_limit, superior_limit))
