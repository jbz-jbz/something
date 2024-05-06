from collections import deque
graph = {
    'A': ['B','C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F'],
    'D': ['B'],
    'E': ['B', 'F'],
    'F': ['C', 'E']
}

def dfs(graph, start, visited=None):
    if visited is None:
        visited = set()
    visited.add(start)
    print(start)
    for i in graph[start]:
        if i not in visited:
            visited.add(i)
            
            dfs(graph,i,visited)
    
def bfs(graph, start, queue, visited=None):
    if not queue:
        return 
    if visited is None:
        visited = {start}
        print(start)
    while queue:
        a = queue.popleft()
        for i in graph[a]:
            if i not in visited:
                visited.add(i)
                queue.append(i)
                print(i)
        bfs(graph,i,queue,visited)
                
    
    
    
dfs(graph, 'A')
queue = deque(['A'])
print("********")
bfs(graph, 'A', queue)

