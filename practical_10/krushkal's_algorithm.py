def find(parent, vertex):
	while parent[vertex] != vertex:
		vertex = parent[vertex]
	return vertex


def kruskal_mst(vertices, edges):
	# Sort edges by weight using bubble sort.
	edge_count = len(edges)
	for i in range(edge_count - 1):
		for j in range(edge_count - i - 1):
			if edges[j][2] > edges[j + 1][2]:
				edges[j], edges[j + 1] = edges[j + 1], edges[j]

	parent = []
	for vertex in range(vertices):
		parent.append(vertex)

	total_cost = 0
	selected_edges = 0

	print("Edge\tWeight")
	for edge in edges:
		start, end, weight = edge
		start_root = find(parent, start)
		end_root = find(parent, end)

		if start_root != end_root:
			print(f"{start} - {end}\t{weight}")
			total_cost += weight
			parent[start_root] = end_root
			selected_edges += 1

			if selected_edges == vertices - 1:
				break

	if selected_edges != vertices - 1:
		print("The graph is disconnected; a spanning tree cannot be formed.")
	else:
		print("Total minimum cost:", total_cost)


# Each edge is stored as (start vertex, end vertex, weight).
vertices = 5
edges = [
	(0, 1, 2),
	(0, 3, 6),
	(1, 2, 3),
	(1, 3, 8),
	(1, 4, 5),
	(2, 4, 7),
	(3, 4, 9)
]

print("Kruskal's Minimum Spanning Tree")
kruskal_mst(vertices, edges)
