def find_the_celebrity(graph):
    ROWS = len(graph)
    # Find the Candidate for celebrity
    candidate = 0
    for i in range(ROWS):
        if graph[candidate][i] == 1:
            candidate = i
    # Verify if its celebrity
    for r in range(ROWS):
        if r != candidate:
            if graph[candidate][i] == 1 or graph[i][candidate] == 0: #If candidate knows a person OR a person does not know a candidate return -1 
                return -1
    return candidate

graph = [
    [1, 1, 0],
    [0, 1, 0],
    [1, 1, 1]
]
print(find_the_celebrity(graph))