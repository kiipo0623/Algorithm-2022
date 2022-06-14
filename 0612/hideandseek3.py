from collections import deque

N, K = map(int, input().split())
dist = [0]*100001
q = deque()
q.append((0, N))

while q:
    cost, now = q.popleft()

    if 0<=now-1<=100000 and (dist[now] == -1 or dist[now] > cost+1):
        dist[now-1] = cost+1
        q.append((dist[now], now-1))

    if 0<=now+1<=100000 and (dist[now] == -1 or dist[now] > cost+1):
        dist[now+1] = cost+1
        q.append((dist[now], now+1))

    if 0<=now*2<=100000 and (dist[now] == -1 or dist[now] > cost):
        dist[now*2] = cost
        q.append((dist[now], now*2))

print(dist[K])