from collections import deque
# 크루스칼 : edge중에서 제일 가까운거 선택
# parent를 자기자신으로 전부 초기화해두고
V, E = map(int, input().split())

edges = []
parent = [i for i in range(V+1)]
print(parent)

for _ in range(E):
    A, B, C = map(int, input().split())
    edges.append((C, A, B))
edges.sort(key = lambda x : x[0])

def find_parent(node):
    if parent[node] != node:
        parent[node] = find_parent(parent[node])
    return parent[node]

def union_parent(node1, node2):
    parA = find_parent(node1)
    parB = find_parent(node2)

    if parA < parB:
        parent[parB] = parA
    else:
        parent[parA] = parB

answer = 0
edges = deque(edges)

while edges:
    cost, nodeA, nodeB = edges.popleft()
    if find_parent(nodeA) != find_parent(nodeB):
        union_parent(nodeA, nodeB)
        answer += cost

print(answer)





