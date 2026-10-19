## Introduction

Kruskal's algorithm finds a minimum spanning tree (MST) for a connected, weighted, undirected graph. It considers edges in increasing order of weight and adds an edge only when it does not create a cycle. This practical orders the edges with bubble sort and uses a parent array to check whether an edge connects different components.

## Conclusion

Kruskal's algorithm builds a minimum spanning tree by selecting the lowest-weight edges that do not form cycles. For the example graph, it connects all five vertices with four edges and a total weight of 16.
