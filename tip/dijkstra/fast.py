import sys
import heapq
input = sys.stdin.readline
INF = int(1e9)

# 노드의 수, 간선의 수
n, m = map(int, input().split())
# 시작 번호 노드
start = int(input())
# 그래프 : 연결 리스트
graph = [[] for _ in range(n+1)] #1-base
# 최단 거리
distance = [INF]*(n+1)

# 간선 정보 입력
for _ in range(m):
    a, b, c = map(int, input().split())
    # a에서 b로 가는 비용이 c
    graph[a].append((b, c))

# 다익스트라
def dijkstra(start):
    distance[start] = 0

    hq = []
    heapq.heappush(hq, (0, start))

    while hq:
        dist, now = heapq.heappop(hq)

        if distance[now] < dist:
            continue

        for node, dist in graph[now]:
            if distance[node] > distance[now] + dist:
                distance[node] = distance[now] + dist
                heapq.heappush(hq, (distance[node], node))

dijkstra(start)

print(distance)