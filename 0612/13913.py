from collections import deque
N, K = map(int, input().split())
q = deque()
cache = [-1]*100001
q.append([N, 0])

if N == K:
    print(0)
    print(N)
    exit()

while True:
    now, cnt = q.popleft()
    if now == K:
        print(cnt)
        ans = str(now)
        now = cache[now]
        while now != N:
            ans = str(now) + ' ' + ans
            now = cache[now]
        ans = str(now) + ' ' + ans
        print(ans)
        break

    if now-1>=0 and cache[now-1] == -1:
        q.append([now-1, cnt+1])
        cache[now-1] = now

    if now+1<=100000 and cache[now+1] == -1:
        q.append([now+1, cnt+1])
        cache[now+1] = now

    if now*2<=100000 and cache[now*2] == -1:
        q.append([now*2, cnt+1])
        cache[now*2] = now
