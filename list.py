tea_varities = ["Black", "Green", "Oolong", "White"]
print(tea_varities)
print(tea_varities[0])
print(tea_varities[-1])
print(tea_varities[1:3])
print(tea_varities[:2])
print(tea_varities[2:])

tea_varities[3] = "Herbal"
print(tea_varities)

# tea_varities[1:2] = "Lemon"
# print(tea_varities)

tea_varities[1:2] = ["Lemon"]
print(tea_varities)

tea_varities[1:3] = ["green","Masala"]
print(tea_varities)

print(tea_varities[1:1])     #output-> []
tea_varities[1:1] = ["test","test"]
print(tea_varities)

print(tea_varities[1:2])
print(tea_varities[1:3])
tea_varities[1:3]=[]
print(tea_varities)

# loop
for i in tea_varities:
    print(i)

for i in tea_varities:
    print(i,end="-")

if "green" in tea_varities:
    print("I have green tea")

tea_varities.append("Oolong")
print(tea_varities)

tea_varities.pop()
print(tea_varities)

tea_varities.remove("green")
print(tea_varities)

tea_varities.insert(1,"Green")
print(tea_varities)

tea_varities_copy = tea_varities.copy()
print(tea_varities_copy)

tea_varities_copy.append("Lemon")
print(tea_varities_copy)
print(tea_varities)

# list comprihence
squared_num=[x**2 for x in range(10)]
print(squared_num)

cube_num=[y**3 for y in range(5)]
print(cube_num)


