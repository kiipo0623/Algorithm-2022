import heapq
INF = float('inf')
def bfs(start):
    global answer
    h = []
    heapq.heappush(h, (0, start))
    visited = [False]*100001
    visited[start] = True

    while h:
        dis, now = heapq.heappop(h)
        if now == K:
            return dis
        if 0<=now*2<=100000 and not visited[now*2]:
            visited[now*2] = True
            heapq.heappush(h, (dis, now*2))


        if 0<=now-1<=100000 and not visited[now-1]:
            visited[now-1] = True
            heapq.heappush(h, (dis+1, now-1))

        if 0<=now+1<=100000 and not visited[now+1]:
            visited[now+1] = True
            heapq.heappush(h, (dis+1, now+1))


N, K = map(int, input().split())
# answer = float('inf')
# bfs(N)
print(bfs(N))