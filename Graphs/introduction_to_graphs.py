"""
Breadth First Search
1. Keep a queue containing the people to check
2. Pop a person from the queue
3. Check if the person is a mango seller
4. If is a mango seller return True else False
"""
from collections import deque

def bfs(graph):
    search_queue = deque(graph["you"])
    visited = set()
    while search_queue:
        curr = search_queue.popleft()
        if curr not in visited:
            if is_mango_seller(curr):
                print(curr, " is a mango seller")
                return True
            else:
                visited.add(curr)
                search_queue += graph[curr] # Enqueue the neighbors
    return False


def is_mango_seller(person):
    return person[-1] == "m"

graph = {}
graph["you"] = ["alice", "bob", "claire"]
graph["bob"] = ["anuj", "peggy"]
graph["alice"] = ["peggy"]
graph["claire"] = ["thom", "jonny"]
graph["anuj"] = []
graph["peggy"] = []
graph["thom"] = []
graph["jonny"] = []

print(bfs(graph))
