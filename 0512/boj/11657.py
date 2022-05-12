import sys
input = sys.stdin.readline
INF = float('inf')

def bellman_ford(start):
    distance = [INF]*(N+1)
    distance[start] = 0

    for v in range(N-1): #edge 개수만큼 진행
        for node in range(1, N+1): # 중간 노드
            for dif_node in graph[node]:
                node2, cost = dif_node
                if distance[node2] > distance[node] + cost:
                    distance[node2] = distance[node] + cost

    # 다 갱신하고 또 갱신될 경우 : return -1
    for node in range(1, N + 1):  # 중간 노드
        for dif_node in graph[node]:
            node2, cost = dif_node
            if distance[node2] > distance[node] + cost:
                return -1
    return distance


N, M = map(int, input().split())
graph = [[] for _ in range(N+1)] # 1번 버스부터 있음

for _ in range(M):
    A, B, C = map(int, input().split())
    graph[A].append((B, C))

res = bellman_ford(1)
if res == -1:
    print(-1)
else:
    for i in range(2, N+1):
        if res[i] < INF:
            print(res[i])
        else:
            print(-1)
