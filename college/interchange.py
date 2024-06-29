example_list = [1, 2, 3, 4, 5]

print("Original list:", example_list)

if len(example_list) > 1:    
    # Swap the first and last elements
    example_list[0], example_list[-1] = example_list[-1], example_list[0]

# Print the list after interchanging first and last elements
print("List after interchanging first and last elements:", example_list)