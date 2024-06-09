# Create a function to transpose a matrix
"""
1 2 3    1 4
4 5 6 => 2 5
         3 6
"""
def transpose_matrix(mat):
    rows, cols = len(mat), len(mat[0])
    transposed_matrix = [[0] * rows for _ in range(cols)]
    for i in range(rows):
        for j in range(cols):
            transposed_matrix[j][i] = mat[i][j]
    return transposed_matrix

matrix = [[1,2,3],[4,5,6]]
#print(transpose_matrix(matrix))

# Create a function to rotate a matrix of dimension n x n,  90 degres.
"""
           0 1 2
        0  1 2 3    1 4 7    7 4 1
        1  4 5 6 => 2 5 8 => 8 5 2
        2  7 8 9    3 6 9    9 6 3
"""
def rotate_matrix_90_degres(matrix):
    l, r = 0, len(matrix) - 1
    while l <= r:
        matrix[l], matrix[r] = matrix[r], matrix[l]
        l += 1
        r -= 1
    matrix_90_degres = list(map(list, zip(*matrix)))
    return matrix_90_degres

def rotate_matrix_with_transpose(matrix):
    matrix = list(map(list, zip(*matrix)))
    for i in range(len(matrix)):
        matrix[i].reverse()
    return matrix

#How to do transpose of n x n in line, got stuck
def rotate_matrix(square_matrix):


matrix_to_rotate = [[1,2,3],[4,5,6],[7,8,9]]
print(rotate_no_extra_memory(matrix_to_rotate))




