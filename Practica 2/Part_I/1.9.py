# 9.	Write a Python program to get the smallest number from a list. 

def smallest_num_in_list( list ):
    min = list[ 0 ]
    for a in list:
        if a < min:
            min = a
    return min
print(smallest_num_in_list([7 ,35 ,2 ,23 ,-5 , 0]))