my_list = [10, 20, 30, 40, 50]

index1 = 1
index2 = 3

# Print original list
print(f"Original list: {my_list}")

if 0 <= index1 < len(my_list) and 0 <= index2 < len(my_list):

    my_list[index1], my_list[index2] = my_list[index2], my_list[index1]
    print(f"List after swapping elements at indices {index1} and {index2}: {my_list}")
else:
    print("Index out of range")
