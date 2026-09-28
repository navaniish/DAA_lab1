# Depth First Search (DFS) Implementation in Python

def dfs_recursive(graph, node, visited=None, traversal_order=None):
    """
    Recursively performs Depth First Search on a graph.
    
    Time Complexity : O(V + E)
                      where V is the number of vertices and E is the number of edges.
    Space Complexity: O(V) for the recursion call stack and visited tracking set.
    """
    if visited is None:
        visited = set()
    if traversal_order is None:
        traversal_order = []

    visited.add(node)
    traversal_order.append(node)

    for neighbor in graph.get(node, []):
        if neighbor not in visited:
            dfs_recursive(graph, neighbor, visited, traversal_order)

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

print("--- Depth First Search (DFS) ---")
print("\nGraph (Adjacency List):")
for node, neighbors in graph.items():
    print(f"  {node} -> {neighbors}")

# Executing DFS
result = dfs_recursive(graph, start_node)

print(f"\nDFS Traversal starting from node '{start_node}':")
print(" -> ".join(result))

print("\n--- Complexity Analysis ---")
print("Time Complexity : O(V + E)")
print("  - V = Number of Vertices")
print("  - E = Number of Edges")
print("Space Complexity: O(V) (Call stack & Visited set)")
