tea_types=("Black","Green","Oolong")

print(type(tea_types))

print(tea_types[0])
print(tea_types[-1])
print(tea_types[1:])

print(len(tea_types))

more_tea=("Herbal","Earl Gray")
all_tea = more_tea + tea_types
# all_tea = more_tea*2
print(all_tea)

if "Green" in all_tea:
    print("I have green tea")

more_tea=("Herbal","Earl Gray","Herbal")
print(more_tea.count("Herbal"))

(black,green,oolong)=tea_types
print(black)
print(green)

mixed_data_tuple = ("abc", 34, True, 40, "male")  # mixed data type
del mixed_data_tuple    # Use `del` to delete the entire tuple.

# print(mixed_data_tuple)

# converting tuple to other data types

my_tuple = (1, 2, 3)
my_list = list(my_tuple)  #conver to lists
print(my_list)
my_list. append (4) # Now you can modify the list
my_tuple = tuple(my_list)  #convert to tuples
print(my_tuple)

my_tuple = (1, 2, 3, 4)
# Remove the element with value 3
my_list = list(my_tuple)
my_list. remove (3)
my_tuple = tuple(my_list)
print(my_tuple)

for item in my_tuple:
    print(item)

# Finding the index
index = my_tuple. index (4)
print(index)

# Creating a 3x3 matrix
matrix = (
(1, 2, 3), (4, 5, 6), (7, 8, 9)
)
print(matrix)

# Iterating through the matrix
for row in matrix:
    for item in row:
        print (item, end=' ')
    print () # For a new line after each row