def GCD(x, y):
    gcd = 1
    if x % y == 0:
        return y
    for k in range(int(y / 2), 0, -1):
        if x % k == 0 and y % k == 0:
            gcd = k
            break  
    return gcd

inferior_limit = int(input("Enter the inferior limit: "))
superior_limit = int(input("Enter the superior limit: "))
print("GCD = ", GCD(inferior_limit, superior_limit))

