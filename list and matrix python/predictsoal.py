#nyari index dari suatu elemen matrix
def searchMatrix(matrix, target):
    if not matrix: return False
    rows, cols = len(matrix), len(matrix[0])
    left, right = 0, rows * cols - 1
    
    while left <= right:
        mid = (left + right) // 2
        # Convert 1D index to 2D coordinates
        num = matrix[mid // cols][mid % cols]
        if num == target:
            return True
        elif num > target:
            right = mid - 1
        else:
            left = mid + 1
    return False



#rotate matrix sebanyak k kali clockwise
def rotateMatrix(mat):
    m, n = len(mat), len(mat[0])
    row, col = 0, 0
    
    while row < m and col < n:
        if row + 1 == m or col + 1 == n:
            break
        
        prev = mat[row + 1][col]

        # Move elements of the first row
        for i in range(col, n):
            curr = mat[row][i]
            mat[row][i] = prev
            prev = curr
        row += 1

        # Move elements of the last column
        for i in range(row, m):
            curr = mat[i][n - 1]
            mat[i][n - 1] = prev
            prev = curr
        n -= 1

        # Move elements of the last row
        if row < m:
            for i in range(n - 1, col - 1, -1):
                curr = mat[m - 1][i]
                mat[m - 1][i] = prev
                prev = curr
        m -= 1

        # Move elements of the first column
        if col < n:
            for i in range(m - 1, row - 1, -1):
                curr = mat[i][col]
                mat[i][col] = prev
                prev = curr
        col += 1
       
# Function to rotate the matrix k times
def rotateMatrixKTimes(mat, k):
    for i in range(k):
        rotateMatrix(mat)

if __name__ == "__main__":
    mat = [
        [1, 2, 3, 4],
        [5, 6, 7, 8],
        [9, 10, 11, 12],
        [13, 14, 15, 16]
    ]

    k = 5  # Rotate the matrix 2 times
    rotateMatrixKTimes(mat, k)

    # Print the rotated matrix
    for row in mat:
        print(" ".join(map(str, row)))



#ngecek kesamaan matriks keknya
def check(a, b):
    n = len(a)
    # Flip columns where matrices differ in the first row
    for j in range(n):
        if (a[0][j] != b[0][j]):
            for i in range(n):
                a[i][j] ^= 1
    # Verify remaining rows can be fixed by single row flips
    for i in range(1, n):
        for j in range(1, n):
            if (a[i][j] ^ b[i][j]) != (a[0][j] ^ b[0][j]):
                return False
    return True