import sys, heapq
input = sys.stdin.readline
# logN만 가능

def sorting():
    h = []
    for idx, val in enumerate(graph):
        if idx == 0:
            continue
        heapq.heappush(h, [-len(val), idx])
    return h

N = int(input())
graph = [[] for _ in range(N+1)]
visited = [0 for _ in range(N+1)]

for _ in range(N-1):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

while all(visited):
    hq = sorting()
    dist, node = heapq.heappop(hq)
    for friend in graph[node]:
        graph[friend].remove(node)
