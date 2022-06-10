# 크루스칼 : 간선길이 짧은 것부터 받아서
# find/union 함수

def find(node):
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

V, E = map(int, input().split())
edges = []
parent = [i for i in range(V+1)]
answer = 0
for _ in range(E):
    edges.append(list(map(int, input().split())))
edges.sort(key = lambda x : x[2])

for i in range(E):
    A, B, cost = edges[i]
    if find(A) != find(B):
        answer += cost
        union(A, B)

print(answer)