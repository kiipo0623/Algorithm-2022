from collections import deque

N, K = map(int, input().split())
queue = deque()
queue.append(N)
dist = [0]*100001

while True:
    now = queue.popleft()
    if now == K:
        print(dist[now])
        break

    for mv in [now-1, now+1, now*2]:
        if 0<=mv<=100000 and dist[mv] == 0:
            dist[mv] = dist[now]+1
            queue.append(mv)
