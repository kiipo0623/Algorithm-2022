import heapq
import sys
input = sys.stdin.readline
INF = int(1e9)

def dijkstra():
    speed = [INF] * (N + 1)
    h = []
    used = {i:-1 for i in range(1, N+1)}
    # 오름차순 : 거리, idx
    heapq.heappush(h, (0, 1))
    speed[1] = 0

    while h:
        dis, idx = heapq.heappop(h)
        if speed[idx] < dis:
            continue

        for node, cost in graph[idx]:
            if speed[node] > dis + cost:
                speed[node] = dis + cost
                used[node] = idx
                heapq.heappush(h, (dis+cost, node))

    return speed, used


N, M = map(int, input().split())
graph = [[] for _ in range(N+1)]

for _ in range(M):
    A, B, C = map(int, input().split())
    graph[A].append((B, C))
    graph[B].append((A, C))

speed, used = dijkstra()

print(N-1)
for key, value in used.items():
    if key != 1:
        print('%d %d'%(key, value))



