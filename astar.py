import heapq


class Node:
    def __init__(self, state, parent=None, g=0.0, h=0.0):
        self.state = state
        self.parent = parent
        self.g = g  
        self.h = h  
        self.f = g + h  

    def __lt__(self, other):
        return self.f < other.f  



def manhattan_heuristic(node, goal_state):
    x1, y1 = node.state
    x2, y2 = goal_state
    return abs(x1 - x2) + abs(y1 - y2)


def a_star(start_state, goal_state, maze, neighbors_fn, heuristic_fn):
    open_set = []
    closed_set = set()
    came_from = {}

    start_node = Node(state=start_state, h=heuristic_fn(Node(start_state), goal_state))
    heapq.heappush(open_set, start_node)
    came_from[start_state] = start_node

    while open_set:
        current_node = heapq.heappop(open_set)

        if current_node.state == goal_state:
            
            path = []
            while current_node:
                path.append(current_node.state)
                current_node = current_node.parent
            return list(reversed(path))

        closed_set.add(current_node.state)

        for neighbor_state in neighbors_fn(current_node.state, maze):
            if neighbor_state in closed_set:
                continue

            tentative_g = current_node.g + 1
            neighbor_h = heuristic_fn(Node(neighbor_state), goal_state)
            neighbor_node = Node(state=neighbor_state, parent=current_node, g=tentative_g, h=neighbor_h)

            
            if neighbor_state not in came_from or tentative_g < came_from[neighbor_state].g:
                came_from[neighbor_state] = neighbor_node
                heapq.heappush(open_set, neighbor_node)

    
    return None



def maze_neighbors(state, maze):
    x, y = state
    height = len(maze)
    width = len(maze[0])

    
    neighbors = [
        (x - 1, y),  # up
        (x + 1, y),  # down
        (x, y - 1),  # left
        (x, y + 1)   # right
    ]

    
    return [
        (nx, ny)
        for (nx, ny) in neighbors
        if 0 <= nx < width and 0 <= ny < height and maze[ny][nx] == 0
    ]



maze = [
    [0, 1, 0, 0, 0],
    [0, 1, 0, 1, 0],
    [0, 0, 0, 1, 0],
    [1, 1, 0, 1, 0],
    [0, 0, 0, 0, 0]
]

start = (0, 0)  # Start at the top-left corner
goal = (4, 4)  # Goal at the bottom-right corner

path = a_star(start, goal, maze, maze_neighbors, manhattan_heuristic)

if path:
    print("Path found:", path)
else:
    print("No path found")
