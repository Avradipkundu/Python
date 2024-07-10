# Sorting a Dictionary by Key
my_dict = {'banana': 3, 'apple': 4, 'pear': 1, 'orange': 2}

# Sort by key
sorted_by_key = dict(sorted(my_dict.items()))

print("Sorted by key:", sorted_by_key)

# Sorting a Dictionary by Value
# my_dict = {'apple': 4, 'banana': 3, 'orange': 2, 'pear': 1}

# Sort by value
sorted_by_value = dict(sorted(my_dict.items(), key=lambda item: item[1]))

print("Sorted by value:", sorted_by_value)
