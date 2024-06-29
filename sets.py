s ={1,2,3}

a=set()  #this the empty set don't use {}

# set is an unordered element
myset = {"apple", "banana", "cherry"}
print(myset)
print(len(myset))  # lenght of sets

myset.add("grape")
print(myset)

myset.remove("banana")
print(myset)

print ("apple" in myset)

#set cannot have duplicate value
myset1 = {"Geeks", "for", "Geeks"}
print(myset1)

#Sets can store a mixture of data types (strings, integers, booleans, etc.)
myset3 = {"Geeks", 10, 52.7, True}
print(myset3)

ch= set("Hello")
print(ch)

# slicing and indexing does not work because set is unordered 
myset4={1,2,3,4}
u=set(myset4)
# print(u[0])
# print(u[0:3])

u.update([50,60])
print(u)
print(myset4)

u.remove(50)
print(u)
print(u.pop())
print(u.pop())


# Union
set1 = {1, 2, 3,}
set2 = {3, 4, 5}
union_result = set1 | set2
print (union_result)

print(set1.union(set2))

# Intersection
union_result = set1 & set2
print (union_result)

print(set1.intersection(set2))

# difference
difference_result = set1 - set2
print ("Difference:", difference_result)

# symmetric
symmetric_diff_result = set1 ^ set2
print ("Symmetric Difference:", symmetric_diff_result)