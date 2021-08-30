

def depthFirstTraversal(graph, current):
    stack = [current]
    while(stack):
        current = stack.pop()
        print(current, end = " ")
        for neighbor in graph[current]:
            stack.append(neighbor)
            
            

graph = {
    'a': ['b','c'],
    'b': ['d'],
    'c': ['e'],
    'd': ['f'],
    'e': [],
    'f': []
}
print("Graph - Adjacency List: ",graph)
depthFirstTraversal(graph, 'a')
