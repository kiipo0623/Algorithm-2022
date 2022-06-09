V, E = map(int, input().split())
edges = []
parent = [i for i in range(V+1)]
for _ in range(E):
	A, B, C = map(int, input().split())
	edges.append((C, A, B))
edges.sort()

def find(node):
	if parent[node] != node:
		parent[node] = find(parent[node])
	return parent[node]

def union(nodeA, nodeB):
	rootA = find(nodeA)
	rootB = find(nodeB)
	if rootA < rootB:
		parent[rootB] = nodeA
	else:
		parent[rootA] = nodeB

MST, edge_cnt, edge_cost = [], 0, 0
for i in range(E):
	cost, A, B = edges[i]
	if find(A) != find(B):
		union(A, B)
		MST.append((A, B))
		edge_cnt += 1
		edge_cost += cost
print(edge_cost)
