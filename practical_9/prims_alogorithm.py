# Prim's Algorithm for Minimum Spanning Tree (MST) in Python

def min_key_vertex(key, mst_set, num_vertices):
    """
    Finds the vertex with the minimum key value from the set of vertices
    not yet included in the MST.
    """
    min_val = float('inf')
    min_index = -1

    for v in range(num_vertices):
        if not mst_set[v] and key[v] < min_val:
            min_val = key[v]
            min_index = v

    return min_index


def prim_mst(graph):
    """
    Computes the Minimum Spanning Tree (MST) using Prim's Algorithm.
    
    Time Complexity : O(V^2) using Adjacency Matrix (without built-in priority queue / heapq).
    Space Complexity: O(V) for storing key, parent, and mst_set arrays.
    """
    num_vertices = len(graph)
    
    # Key values used to pick minimum weight edge in cut
    key = [float('inf')] * num_vertices
    
    # Array to store constructed MST
    parent = [-1] * num_vertices
    
    # Track vertices included in MST
    mst_set = [False] * num_vertices

    # Start from vertex 0
    key[0] = 0

    for _ in range(num_vertices):
        # Pick the minimum key vertex from unvisited set
        u = min_key_vertex(key, mst_set, num_vertices)
        
        if u == -1:
            break

        mst_set[u] = True

        # Update key and parent for adjacent vertices
        for v in range(num_vertices):
            # graph[u][v] > 0 indicates an edge between u and v
            if graph[u][v] > 0 and not mst_set[v] and graph[u][v] < key[v]:
                key[v] = graph[u][v]
                parent[v] = u

    # Print MST Edges and compute total minimum cost
    print("Edge \tWeight")
    total_cost = 0
    for i in range(1, num_vertices):
        print(f"{parent[i]} - {i} \t  {graph[i][parent[i]]}")
        total_cost += graph[i][parent[i]]
        
    print(f"\nTotal Minimum Cost of Spanning Tree: {total_cost}")


# Hardcoded Weighted Graph Representation (Adjacency Matrix - No User Input)
# Vertices: 0, 1, 2, 3, 4
graph = [
    [0, 2, 0, 6, 0],
    [2, 0, 3, 8, 5],
    [0, 3, 0, 0, 7],
    [6, 8, 0, 0, 9],
    [0, 5, 7, 9, 0]
]

print("--- Prim's Minimum Spanning Tree (MST) Algorithm ---")
print("\nAdjacency Matrix:")
for row in graph:
    print(f"  {row}")

print("\nMinimum Spanning Tree (MST) Edges:")
prim_mst(graph)

print("\n--- Complexity Analysis ---")
print("Time Complexity : O(V^2)")
print("  - V = Number of Vertices")
print("Space Complexity: O(V) (Key, Parent, and MST tracking arrays)")
