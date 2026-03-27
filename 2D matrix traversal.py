
matrix = [
    [1,2,3],
    [4,5,6],
    [7,8,9]
]

rows = len(matrix)
cols = len(matrix[0])

# here we do Row-wise Traversal
print("Row-wise Traversal:")
for i in range(rows):
    for j in range(cols):
        print(matrix[i][j], end=" ")
    print()

#here we do Column-wise Traversal
print("\nColumn-wise Traversal:")
for j in range(cols):
    for i in range(rows):
        print(matrix[i][j], end=" ")
    print()

#now we do total sum of all elements in the matrix
total = 0
for i in range(rows):
    for j in range(cols):
        total += matrix[i][j]
print("\nSum of elements:", total)

# searching for an element in the matrix
key = 5
found = False
for i in range(rows):
    for j in range(cols):
        if matrix[i][j] == key:
            print(f"Element {key} found at position ({i},{j})")
            found = True
if not found:
    print("Element not found")

# transpose of the matrix
print("\nTranspose:")
for j in range(cols):
    for i in range(rows):
        print(matrix[i][j], end=" ")
    print()