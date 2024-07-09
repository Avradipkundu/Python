def list_of_tuples_with_cubes(numbers):
    return [(num, num**3) for num in numbers]

# Example usage
numbers = [1, 2, 3, 4, 5]
result = list_of_tuples_with_cubes(numbers)
print(result)

