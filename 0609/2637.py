from collections import deque

N = int(input())
M = int(input())

need = [0 for _ in range(N+1)] # 몇개필요한지
inDegree = [0 for _ in range(N+1)]
graph = [[] for _ in range(N+1)]

# 시작점 무조건 N

for _ in range(M):
    X, Y, K = map(int, input().split())
    inDegree[Y] += 1
    graph[X].append((Y, K))

need[N] = 1
queue = deque()
queue.append(N)

while queue:
    now = queue.popleft()
    for node, cnt in graph[now]:
        inDegree[node] -= 1
        need[node] += cnt*need[now]
        if inDegree[node] == 0:
            queue.append(node)

for i in range(1, N+1):
    if len(graph[i]) == 0:
        print(i, need[i])