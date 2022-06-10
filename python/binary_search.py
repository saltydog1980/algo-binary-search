import random
test_array = [1,2,3,4,5]
super_big_array = [1,5,7,2,3,8,4,9]
def binary_search(target, coll):
    coll.sort()
    index_to_check = round(len(coll)/2)
    check = True
    while check:
        if target > len(coll):
            check = False
            return -1
        if coll[index_to_check] == target:
            return index_to_check 
        elif coll[index_to_check] > target:
            index_to_check = round(index_to_check/2)
        elif coll[index_to_check] < target:
            index_to_check = (round(index_to_check/2) + index_to_check)
        else:    
            check = False
            return -1
    
print(binary_search(7, super_big_array))


















