import sys, heapq
input = sys.stdin.readline
N, M, X = map(int, input().split())
INF = float('inf')

graph = [[] for _ in range(N+1)]

for _ in range(M):
    a, b, T = map(int, input().split())
    graph[a].append((b, T))

def dijkstra(start):
    h = []
    heapq.heappush(h, (0, start))
    distance = [INF]*(N+1)
    distance[start] = 0

    while h:
        dis, now = heapq.heappop(h)
        if dis > distance[now]:
            continue
        for node, cost in graph[now]:
            if distance[node] > dis + cost:
                distance[node] = dis + cost
                heapq.heappush(h, (dis+cost, node))

    return distance

distance = dijkstra(X)

for i in range(1, N+1):
    if i == X: continue
    d = dijkstra(i)
    distance[i] += d[X]

MAX = 0
for i in range(1, N+1):
    if i == X:continue
    MAX = max(MAX, distance[i])

print(MAX)