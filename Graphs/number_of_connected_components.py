# Union find problem
def count_components(n, edges):
    parent = [i for i in range(n)]
    rank = [1] * n

    def find(node_1):
        res = node_1
        while res != parent[res]:
            parent[res] = parent[parent[res]]
            res = parent[res]
        return res
    
    def union(node_1, node_2):
        parent_1, parent_2 = find(node_1), find(node_2)
        if parent_1 == parent_2:
            return 0
        if rank[parent_2] > rank[parent_1]:
            parent[parent_1] = parent_2
            rank[parent_2] += rank[parent_1]
        else:
            parent[parent_2] = parent_1
            rank[parent_1] += rank[parent_2]
        return 1

    res = n
    for node_1, node_2 in edges:
        res -= union(node_1, node_2)
    return res