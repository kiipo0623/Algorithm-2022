# 프림
# 선택되지 않은 것들 중 가장 가까운 것 선택
# heapq를 사용하면 더 빠르다
import heapq
V, E = map(int, input().split())
graph = [[] for _ in range(V+1)]
for _ in range(E):
    A, B, C = map(int, input().split())
    graph[A].append((C, B))
    graph[B].append((C, A))

# 거리, 노드
h = [(0, 1)]
selected = [True] + [False]*V
answer = 0

while h:
    dist, node = heapq.heappop(h)
    if selected[node]:
        continue
    selected[node] = True
    answer += dist
    for n in graph[node]:
        if not selected[n[1]]:
            heapq.heappush(h, n)

print(answer)