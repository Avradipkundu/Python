list=[1,2,3,4,5,6,7,8,9]

# Using len() Function
length1=len(list)
print("Length of the list: ",length1)

# Using a Loop
length=0
for i in list:
    length+=1
print("Length of the list: ",length)

# Using List Comprehension
length2=sum([1 for _ in list])
print("Length of the list: ",length2)
