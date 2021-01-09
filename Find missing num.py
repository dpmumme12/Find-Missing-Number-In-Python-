def finder(arr1, arr2):
    counter = {}
    
    for num in arr1:
        if num in counter:
            counter[num] += 1  
        else:
            counter[num] = 1
        
    for num in arr2:
        if num in counter:
            counter[num] -= 1  
        if counter[num] == 0:
            del counter[num]
    
    return list(counter)[0]

lst1 = [int(x) for x in input("Numbers in first list (put spaces between numbers): ").split()]
lst2 = [int(x) for x in input("Numbers in second list (put spaces between numbers): ").split()]

print(f'Missing number is: {finder(lst1,lst2)}')
