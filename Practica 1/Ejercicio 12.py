def sum(limit):
    total_sum = 0
    for i in range(3, limit+1):
        if (i%3 == 0 or i%5 == 0):
            total_sum += i
    print(total_sum) 

                 
limit = int(input("Enter limit: "))
sum(limit)
