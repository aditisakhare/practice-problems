

def depthFirstTraversal(graph, current):
    stack = [current]
    while(stack):
        current = stack.pop()
        print(current, end = " ")
        for neighbor in graph[current]:
            stack.append(neighbor)
            
def depthFirstTraversalRec(graph, current):
    print(current, end = " ")
    for neighbor in graph[current]:
        depthFirstTraversalRec(graph, neighbor)
                

graph = {
    'a': ['b','c'],
    'b': ['d'],
    'c': ['e'],
    'd': ['f'],
    'e': [],
    'f': []
}
print("Graph - Adjacency List: ",graph)
print("Depth First Traversal: ")
depthFirstTraversal(graph, 'a') #acebdf #abdfce
print("\n")
print("Depth First Traversal Recursion: ",)
depthFirstTraversalRec(graph,'a')

#Time complexity: O(V+E)
