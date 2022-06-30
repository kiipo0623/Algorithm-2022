import heapq
def dijkstra(start):
    h = []
    distance = [INF]*(N+1)
    distance[start] = 0
    # 거리, 노드
    heapq.heappush(h, [0, start])
    while h:
        dist, now = heapq.heappop(h)
        for node in graph[now]:
            if distance[node] > dist + 1:
                distance[node] = dist+1
                heapq.heappush(h, [distance[node], node])
    return distance

INF = int(1e9)
N, M, K, X = map(int, input().split())
graph = [[] for _ in range(N+1)]
for _ in range(M):
    A, B = map(int, input().split())
    graph[A].append(B)

dis = dijkstra(X)

flag = False
for i in range(1, N+1):
    if dis[i] == K:
        flag = True
        print(i)

if not flag:
    print(-1)
