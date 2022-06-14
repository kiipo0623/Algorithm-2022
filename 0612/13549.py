import heapq

N, K = map(int, input().split())
dist = [-1]*100001
dist[N] = 0
h = [(0, N)]
heapq.heapify(h)

while h:
    cost, now = heapq.heappop(h)
    if now == K:
        print(cost)
        break

    if 0<=now*2<=100000 and dist[now*2] == -1:
        dist[now*2] = cost
        heapq.heappush(h, (dist[now*2], now*2))

    if 0<=now-1<=100000 and dist[now-1] == -1:
        dist[now-1] = cost+1
        heapq.heappush(h, (dist[now-1], now-1))

    if 0<=now+1<=100000 and dist[now+1] == -1:
        dist[now+1] = cost+1
        heapq.heappush(h ,(dist[now+1], now+1))

