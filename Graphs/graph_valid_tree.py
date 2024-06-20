def valid_tree(n, edges):

    if not n:
        return True
    adj = {i:[] for i in range(n)}

    # Undirected graph
    for node_1, node_2 in edges:
        adj[node_1].append(node_2)
        adj[node_2].append(node_1)
    print(adj)

    visited = set()

    def dfs(node, prev):
        if node in visited:
            return False
        visited.add(node)
        for i in adj[node]:
            if i == prev:
                continue
            if not dfs(i, node):
                return False
        return True
    
    return dfs(0, -1) and n == len(visited)


    
n = 5
edges = [[0,1], [0,2], [0, 3], [1, 4]]
print(valid_tree(n, edges))