
def is_safe(color_assignment, adj_matrix, color, node):
    
    for neighbor in range(len(adj_matrix)):
        if neighbor != node and color_assignment[neighbor] == color and adj_matrix[node][neighbor] == 1:
            return False
    return True


def solve(adj_matrix, color_assignment, num_colors, num_nodes, node):
    if node == num_nodes:
       
        return True

    
    for color in range(1, num_colors + 1):
        if is_safe(color_assignment, adj_matrix, color, node):
            color_assignment[node] = color
            
            if solve(adj_matrix, color_assignment, num_colors, num_nodes, node + 1):
                return True
            
            color_assignment[node] = 0

    return False


def main():
    
    adj_matrix = [
        [0, 1, 1, 0],  
        [1, 0, 1, 1],  
        [1, 1, 0, 1],  
        [0, 1, 1, 0]   
    ]

    num_nodes = len(adj_matrix)
    color_assignment = [0] * num_nodes
    num_colors = 4  

    if solve(adj_matrix, color_assignment, num_colors, num_nodes, 0):
        print("Graph successfully colored:")
        for node in range(num_nodes):
            print(f"Node {node} - Color {color_assignment[node]}")
    else:
        print("Could not color the graph with the given number of colors")




main()
