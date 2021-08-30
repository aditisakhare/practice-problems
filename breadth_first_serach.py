
from collections import deque

def breadthFirstTraversal(graph,current):
    queue = deque()
    queue.appendleft(current)
    while(queue):
        current = queue.pop()
        print(current)
        for neighbor in graph[current]:
            queue.appendleft(neighbor)
        



graph = {
    'a': ['b','c'],
    'b': ['d'],
    'c': ['e'],
    'd': ['f'],
    'e': [],
    'f': []
}
print("Graph - Adjacency List: ",graph)
print("Breadth First Traversal: ")
breadthFirstTraversal(graph, 'a') #acebdf #abdfce
print("\n")