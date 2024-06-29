# Example tuple
tup = (8, 1, 7, 3, 2, 9, 4, 6, 5)
k = 3

# Convert tuple to list
lst = list(tup)

# Sort the list
lst.sort()

# Get the first k elements (minimum k elements)
min_k_elements = lst[:k]

# Get the last k elements (maximum k elements)
max_k_elements = lst[-k:]

# Print the results
print(f"Minimum {k} elements: {min_k_elements}")
print(f"Maximum {k} elements: {max_k_elements}")
