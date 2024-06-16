from collections import deque

def walls_and_gates(rooms):

    def add_rooms(r, c):
        if (r >=  ROWS or c >= COLS or r < 0 or c < 0 or (r,c) in visited or rooms[r][c] == -1):
            return
        visited.add((r,c))
        q.append((r,c))

    ROWS, COLS = len(rooms), len(rooms[0])
    visited = set()
    q = deque()
    
    # Marking the existing gates
    for r in range(ROWS):
        for c in range(COLS):
            if rooms[r][c] == 0:
                q.append((r, c))
                visited.add((r,c))
    
    distance = 0
    while q:
        for i in range(len(q)):
            r, c = q.popleft()
            rooms[r][c] = distance
            add_rooms(r + 1, c)
            add_rooms(r - 1, c)
            add_rooms(r, c + 1)
            add_rooms(r, c - 1)
        distance += 1    

    return rooms

rooms = [
    [float('inf'), -1, 0, float('inf')],
    [float('inf'), float('inf'), float('inf'), -1],
    [float('inf'), -1, float('inf'), -1],
    [0, -1, float('inf'), float('inf')]
]

print(walls_and_gates(rooms))
