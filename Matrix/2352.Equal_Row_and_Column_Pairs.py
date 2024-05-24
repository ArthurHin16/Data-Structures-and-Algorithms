"""
Given a 0-indexed n x n integer matrix grid, return the number of pairs (ri, cj) such that 
row ri and column cj are equal.
"""


def equalPairs(grid):
    rows = grid  # Directly use grid as rows
    # Transpose the grid to get columns
    transposed_matrix = list(map(list, zip(*grid)))
    print(transposed_matrix)
    counter = 0
    for i in range(len(rows)):
        for j in range(len(transposed_matrix)):
            if rows[i] == transposed_matrix[j]:
                counter += 1

    return counter


grid = [[3, 2, 1], [1, 7, 6], [2, 7, 7]]
print(equalPairs(grid))
