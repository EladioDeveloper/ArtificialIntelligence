def primeNumbers(limit):
    for i in range (2, limit+1):
        for j in range(2, i):
            if i%j == 0:
                break
        else:
            print(i)

limit=int(input("Enter the limit: "))
primeNumbers(limit)