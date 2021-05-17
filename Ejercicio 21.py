def permutation(list):
    if len(list) == 0:
        return []
    elif len(list) == 1:
        return [list]
    else:
        permutation_list = []
        for i in range(len(list)):
            m = list[i]
            remainig_list = list[:i] + list[i+1:]
        for p in permutation(remainig_list):
            permutation_list.append([m] + p)
            
    return permutation_list

x  = 1
for p in permutation(['a','e','i','o','u']):
    print(x, '. ', p)
    x += 1
