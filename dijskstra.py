import heapq

def dijkstra(n,graph,start):
    distances = [float('inf')]*n
    distances[start] = 0
    priQ = [(0,start)]
    while priQ:
        current_weight, edge = heapq.heappop(priQ)
        if current_weight > distances[edge]:
            continue 
        for neighbour, weight in graph[edge]:
            distance = weight+current_weight
            if distance<distances[neighbour]:
                distances[neighbour] = distance
                heapq.heappush(priQ,(distance, neighbour))
    return distances
    
num_vertices = 5


adjacency_list = {
    0: [(1, 10), (3, 30), (4, 100)],
    1: [(2, 50)],
    2: [(4, 10)],
    3: [(2, 20), (4, 60)],
    4: [],
}


start_node = 0


shortest_paths = dijkstra(num_vertices, adjacency_list, start_node)


print(f"Shortest paths from node {start_node}:")
for i, dist in enumerate(shortest_paths):
    print(f"To node {i}: {dist}")
