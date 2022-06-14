from collections import deque
N, K = map(int, input().split())
dist = [-1]*100001
cnt = [0]*100001
dist[N] = 0
cnt[N] = 1

q = deque()
q.append(N)
# dist랑 같으면 cnt올리다가 dist보다 크면 break

while q:
    now = q.popleft()

    for mv in [now-1, now+1, now*2]:
        if 0<=mv<=100000:
            if dist[mv] < 0 or dist[mv] == dist[now]+1:
                dist[mv] = dist[now]+1
                cnt[mv] += 1
                q.append(mv)

print(dist[K])
print(cnt[K])
