# Breadth First Search (BFS) Implementation in Python

def bfs(graph, start_node):
    """
    Performs Breadth First Search on a graph level by level using a queue.
    
    Time Complexity : O(V + E)
                      where V is the number of vertices and E is the number of edges.
    Space Complexity: O(V) for queue storage and visited tracking set.
    """
    visited = set()
    queue = []
    traversal_order = []

    # Initialize queue with start node
    visited.add(start_node)
    queue.append(start_node)

    while queue:
        # Dequeue front element
        current_node = queue.pop(0)
        traversal_order.append(current_node)

        # Explore all unvisited neighbors
        for neighbor in graph.get(current_node, []):
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)

    return traversal_order


# Hardcoded Graph representation using Adjacency List (No user input required)
graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': ['F'],
    'F': []
}

start_node = 'A'

print("--- Breadth First Search (BFS) ---")
print("\nGraph (Adjacency List):")
for node, neighbors in graph.items():
    print(f"  {node} -> {neighbors}")

# Executing BFS
result = bfs(graph, start_node)

print(f"\nBFS Traversal starting from node '{start_node}':")
print(" -> ".join(result))

print("\n--- Complexity Analysis ---")
print("Time Complexity : O(V + E)")
print("  - V = Number of Vertices")
print("  - E = Number of Edges")
print("Space Complexity: O(V) (Queue & Visited set)")
