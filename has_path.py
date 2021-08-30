graph = {
    'a': ['b','c'],
    'b': ['d'],
    'c': ['e'],
    'd': ['f'],
    'e': [],
    'f': []
}

def has_path(graph, current, dest):
    if current == dest:
        return 1
    for neighbor in graph[current]:
        if has_path(graph, neighbor, dest):
            return 1
    return 0
    

if has_path(graph,'a','f'):
    print("Element has a path")
else:
    print("No path found")

if has_path(graph,'b','e'):
    print("Element has a path")
else:
    print("No path found")
