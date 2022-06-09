V, E = map(int, input().split())
graph = []
for _ in range(E):
    graph.append(list(map(int, input().split())))

graph.sort(key = lambda x:-x[2])

parent = [i for i in range(V+1)]

def find(node):
    global parent
    if node != parent[node]:
        parent[node] = find(parent[node])
    return parent[node]

def union(nodeA, nodeB):
    parA = find(nodeA)
    parB = find(nodeB)
    if parA < parB:
        parent[parB] = parA
    else:
        parent[parA] = parB

MST, tree_edges, mst_cost = [], 0, 0


while True:
    if tree_edges == V-1:
        break
    u, v, wt = graph.pop()
    if find(u) != find(v):
        union(u, v)
        MST.append((u, v))
        mst_cost += wt
        print(u, v, wt, mst_cost)
        tree_edges += 1

print(mst_cost)
