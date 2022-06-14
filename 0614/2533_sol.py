import sys
sys.setrecursionlimit(10**9)
input = sys.stdin.readline
n = int(input())
c = [[] for _ in range(n+1)]
dp = [[0, 0] for _ in range(n+1)]

for _ in range(n-1):
    a, b = map(int, input().split())
    c[a].append(b)
    c[b].append(a)

visited = [0 for _ in range(n+1)]

def dfs(start):
    global c, visited
    visited[start] = 1
    if len(c[start]) == 0: # 연결된 것들이 없으면
        dp[start][1] = 1 # 내가 얼리어답터인 경우 수
        dp[start][0] = 0 # 내가 얼리어답터아닌 경우 수

    else:
        for i in c[start]:
            if visited[i] == 0:
                dfs(i)
                dp[start][1] += min(dp[i][0], dp[i][1])
                dp[start][0] += dp[i][1]
        dp[start][1] += 1 # 나 자신

dfs(1)
print(min(dp[1][0], dp[1][1]))
