from collections import deque

def rotten_oranges(grid):

    fresh_oranges = 0
    queue = deque()
    ROWS, COLS = len(grid), len(grid[0])

    for r in range(ROWS):
        for c in range(COLS):
            if grid[r][c] == 1:
                fresh_oranges += 1
            if grid[r][c] == 2:
                queue.append((r,c))
    print(fresh_oranges)
    print(queue)
    
    time = 0
    directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]
    while fresh_oranges > 0 and queue:
        length = len(queue)
        for i in range(length):
            r, c = queue.popleft()
            for dr, dc in directions:
                row, col = r + dr, c + dc
                if (row in range(ROWS) and col in range(COLS) and grid[row][col] == 1):
                    grid[row][col] = 2
                    queue.append((row, col))
                    fresh_oranges -= 1
        time += 1 
    return time if fresh_oranges == 0 else -1   



    

grid = [
    [2,1,1],
    [1,0,0],
    [0,0,1]
]
print("Total time: ", rotten_oranges(grid))