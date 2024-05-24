"""
You are given an n x n 2D matrix representing an image, rotate the image by 90 degrees (clockwise).
"""


def rotate(matrix):
    l, r = 0, len(matrix) - 1
    while l < r:
        matrix[l], matrix[r] = matrix[r], matrix[l]
        l += 1
        r -= 1
    transpose_matrix = list(map(list, zip(*matrix)))
    return transpose_matrix

matrix = [[1,2,3],[4,5,6],[7,8,9]]
print(rotate(matrix))