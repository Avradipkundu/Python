# def list_of_tuples_with_cubes(numbers):
#     return [(num, num**3) for num in numbers]

# numbers = [1, 2, 3, 4, 5]
# result = list_of_tuples_with_cubes(numbers)
# print(result)

list = [1,2,4,5]

listCube = []
for i in list:
    tup = (i,i**3)
    listCube.append(tup)

print(listCube)