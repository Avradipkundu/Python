def have_common_element(list1, list2):
    # Convert list1 to set
    set1 = set(list1)
    # Check if any element in list2 is in set1
    for element in list2:
        if element in set1:
            return True
    return False

list1 = [1, 2, 3, 4, 5]
list2 = [5, 6, 7, 8, 9]
list3 = [10, 11, 12]

print(have_common_element(list1, list2))  
print(have_common_element(list1, list3))  