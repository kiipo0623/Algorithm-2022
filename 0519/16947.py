import sys
sys.setrecursionlimit(10**4)

N = int(input())
graph = [[] for _ in range(N+1)]

for _ in range(N):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

parent = [0] + [-1]*(N)
visited = [True] + [False]*(N)
cycle = []

# cycle찾기
def dfs(start):
    global parent, visited, cycle
    visited[start] = True

    for node in graph[start]:
        if node == parent[start]: # 부모 노드로 안감
            continue
        if visited[node]:
            cycle = [start, node]
            return
        parent[node] = start
        dfs(node)

from collections import deque
def bfs(start):
    q = deque()
    visited = [start]
    q.append((0, start))
    MIN = float('inf')

    while q:
        dist, now = q.popleft()
        if now in cycle:
            return dist
        for node in graph[now]:
            if node not in visited:
                visited.append(node)
                q.append((dist+1, node))
    return MIN



dfs(1)
now = cycle[-1]
# cycle에 해당하는 거 다 잡기
while True:
    if parent[now] not in cycle:
        cycle.append(parent[now])
        now = parent[now]
    else:
        break

answer = []
for i in range(1, N+1):
    if i in cycle:
        answer.append(0)
    else:
        answer.append(bfs(i))

print(' '.join(map(str, (answer))))

