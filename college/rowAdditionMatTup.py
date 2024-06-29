matrix = (
(1, 2, 3), (4, 5, 6), (7, 8, 9)
)

row_sumss=[]
print(matrix)

# Iterating through the matrix
for row in matrix:
    row_sum=0
    for item in row:
        row_sum=row_sum+item

    # row_sumss=list(row_sums)
    row_sumss.append(row_sum)

    # row_sums = row_sums + (row_sum,)
print("RowWise sum:",row_sumss) 
