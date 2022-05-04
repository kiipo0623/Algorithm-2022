import sys
input = sys.stdin.readline
INF = int(1e9)

# 노드의 수, 간선의 수
n, m = map(int, input().split())
# 시작 번호 노드
start = int(input())
# 그래프 : 연결 리스트
graph = [[] for _ in range(n+1)] #1-base
# 방문 정보
visited = [False]*(n+1)
# 최단 거리
distance = [INF]*(n+1)

# 간선 정보 입력
for _ in range(m):
    a, b, c = map(int, input().split())
    # a에서 b로 가는 비용이 c
    graph[a].append((b, c))

def get_smallest():
    min_, minidx = INF, -1
    for i in range(1, n+1):
        if not visited[i] and distance[i] < min_:
            min_, minidx = distance[i], i
    return minidx

# 다익스트라
def dijkstra(start):
    visited[start] = True
    distance[start] = 0

    for node, dist in graph[start]:
        distance[node] = dist

    for _ in range(n-1):
        now = get_smallest()
        visited[now] = True
        for node, dist in graph[now]:
            if distance[node] > distance[now] + dist:
                distance[node] = distance[now] + dist

dijkstra(start)

print(distance)