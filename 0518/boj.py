from collections import deque
N = int(input())
dp = [0]*1000001
q = deque()
q.append(1)

while q:
    now = q.popleft()
    if now+1 < 1000001 and dp[now+1] == 0:
        dp[now+1] = dp[now]+1
        q.append(now+1)
    if now*2 < 1000001 and dp[now*2] == 0:
        dp[now*2] = dp[now]+1
        q.append(now*2)
    if now*3 < 1000001 and dp[now*3] == 0:
        dp[now*3] = dp[now]+1
        q.append(now*3)

print(dp[N])
