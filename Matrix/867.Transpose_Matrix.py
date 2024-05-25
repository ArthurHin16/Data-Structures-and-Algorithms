# Given a 2D integer array matrix, return the transpose of matrix.

def transpose(matrix):
    rows, cols = len(matrix), len(matrix[0])
    result = [[0] * rows for _ in range(cols)]
    for r in range(rows):
        for c in range(cols):
            result[c][r] = matrix[r][c]
    return result


matrix = [[7, 8, 9]]
print(transpose(matrix))
