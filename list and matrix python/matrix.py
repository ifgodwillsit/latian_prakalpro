#buat matrix yh
rows = int(input("rows: "))
col = int(input("columns: "))

matrix = [] 
print("entries row-wise:")

for i in range(rows):   
    row = []
    for j in range(col):
        row.append(int(input()))    # user input for rows
    matrix.append(row)  # adding rows to the matrix

print("\n3D matrix is:")

for i in range(rows):
    for j in range(col):
        print(matrix[i][j], end=" ")
    print()



# penjumlahan matriks pake looping
y = [[1, 2, 3], [3, 4, 5], [5, 6, 7]]
res = [[0]*3 for _ in range(3)]

for i in range(len(matrix)):
    for j in range(len(matrix[0])):
        res[i][j] = matrix[i][j] + y[i][j]

for r in res:
    print(r)

# penjumlahan matriks pake list comprehension
add_res = [[matrix[i][j] + y[i][j] for j in range(len(matrix[0]))] for i in range(len(matrix))]

# pengurangan matriks pake list comprehension
sub_res = [[matrix[i][j] - y[i][j] for j in range(len(matrix[0]))] for i in range(len(matrix))]


print("Matrix Addition:")
for row in add_res:
    print(row)

print("\nMatrix Subtraction:")
for row in sub_res:
    print(row)

# Element-wise multiplication
mult_res = [[matrix[i][j] * y[i][j] for j in range(col)] for i in range(col)]

# Element-wise integer division
div_res = [[matrix[i][j] // y[i][j] for j in range(col)] for i in range(col)]

print("Matrix Multiplication:")
for row in mult_res:
    print(row)

print("\nMatrix Division:")
for row in div_res:
    print(row)

#transpose matriks
transpose = [[matrix[j][i] for j in range(len(matrix))] for i in range(len(matrix[0]))]
print("Matrix transpose")
for t in transpose:
    print(t)