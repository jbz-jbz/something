import heapq
from collections import defaultdict

class Graph:
    def __init__(self):
        self.edges = defaultdict(list)
        
    def addedge(self, u, v, weight):
        self.edges[u].append((v,weight))
        self.edges[v].append((u,weight))
        
def prims(graph, start):
    minH = []
    mst = []
    visited = set()
    total_cost= 0 
    
    for edge in graph.edges[start]:
        heapq.heappush(minH,(edge[1],start,edge[0]))
        
    while minH:
        weight, u, v = heapq.heappop(minH)
        
        if v not in visited:
            visited.add(v)
            visited.add(u)
            total_cost+=weight
            mst.append((u,v,weight))
            for edge in graph.edges[v]:
                heapq.heappush(minH,(edge[1],v,edge[0]))
                
    return mst, total_cost 
    
g = Graph()
g.addedge('A','B',10)
g.addedge('A', 'C', 41)
g.addedge('B', 'C', 2)
g.addedge('B', 'D', 5)
g.addedge('C', 'D', 3)

arr, t = prims(g,'A')
print(arr)
print(t)

        
        
        
        
        
        
        
        
        
        
        
        
        
