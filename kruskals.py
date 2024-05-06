
edges = [
    ('A', 'B', 1),
    ('A', 'C', 3),
    ('B', 'C', 1),
    ('B', 'D', 6),
    ('C', 'D', 5),
    ('C', 'E', 2),
    ('D', 'E', 2),
    ('D', 'F', 4),
    ('E', 'F', 3),
]


class UnionFind:
    def __init__(self, elements):
        self.parent = {x: x for x in elements}
        self.rank = {x: 0 for x in elements}

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])  
        return self.parent[x]

    def union(self, x, y):
        rootX = self.find(x)
        rootY = self.find(y)

        if rootX != rootY:
            
            if self.rank[rootX] < self.rank[rootY]:
                self.parent[rootX] = rootY
            elif self.rank[rootX] > self.rank[rootY]:
                self.parent[rootY] = rootX
            else:
                self.parent[rootY] = rootX
                self.rank[rootX] += 1


def kruskal(nodes, edges):
    
    edges = sorted(edges, key=lambda x: x[2])

  
    uf = UnionFind(nodes)

    mst = []  
    for edge in edges:
        node1, node2, weight = edge
        
        if uf.find(node1) != uf.find(node2):
            mst.append(edge)
            uf.union(node1, node2)

    return mst



nodes = set(['A', 'B', 'C', 'D', 'E', 'F'])
mst = kruskal(nodes, edges)

print("Minimum Spanning Tree:")
for edge in mst:
    print(edge)
