"""
    adj = {
        0: [1, 3],
        1: [3, 0, 1],
        2: [2],
        3: [0]    
    }
"""
from collections import deque

def keys_and_rooms(rooms):

    number_of_rooms = len(rooms)
    adj = {i: [] for i in range(number_of_rooms)}
    for i in range(number_of_rooms):
        adj[i] += rooms[i]

    # BFS Is there a path to every node?
    queue = deque(rooms[0])
    visited = set()
    traversal_order = set({0})
    while queue:
        queue_size = len(queue)
        for i in range(queue_size):
            curr = queue.popleft()
            if curr not in visited:
                visited.add(curr)
                traversal_order.add(curr)
                queue += adj[curr]
    return True if number_of_rooms == len(traversal_order) else False

def keys_and_rooms_improved(rooms):
    number_of_rooms = len(rooms)
    queue = deque([0])
    visited = set([0])
    total_visited = 1

    while queue:
        curr = queue.popleft()
        for neighbor in rooms[curr]:
            if neighbor not in visited:
                total_visited += 1
                visited.add(neighbor)
                queue.append(neighbor)
    
    return total_visited == number_of_rooms



rooms = [[1,3],[3,0,1],[2],[0]]
print(keys_and_rooms(rooms))
print(keys_and_rooms_improved(rooms))