import heapq
V, E = map(int, input().split())
graph = [[] for _ in range(V+1)]
for _ in range(E):
	u, v, w = map(int, input().split())
	graph[u].append((v, w))
	graph[v].append((u, w))

answer = 0

q = [(0, 1)] # cost, node
visited = [True] + [False]*(V)
heapq.heapify(q)

while q:
    w, d = heapq.heappop(q)
    if visited[d]:
        continue
    visited[d] = True
    answer += w
    for e in graph[d]:
        e_d, e_w = e
        heapq.heappush(q, (e_w, e_d))
print(answer)