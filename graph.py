graph = {
    'A': [('B', 5), ('C', 3)],
    'B': [('D', 2)],
    'C': [('D', 7)],
    'D': []
}

print("Directed Weighted Graph (Adjacency List):")

for node in graph:
    print(node, "->", graph[node])