import sys
sys.setrecursionlimit(10**6)
s = []
tree = [[] for _ in range(300001)]
dp = [[0] * 2 for _ in range(300001)]
INF = int(1e9)


def dfs(now):
    if not tree[now]:
        dp[now][0], dp[now][1] = s[now], 0
        return

    dp[now][0] = s[now]
    cost = INF
    for son in tree[now]:
        dfs(son)
        dp[now][0] += min(dp[son])
        cost = min(cost, dp[son][0] - dp[son][1])  # 참석했을 때의 손해

    if cost < 0:
        cost = 0

    dp[now][1] = dp[now][0] + cost - s[now]


def solution(sales, links):
    global s
    s = [0] + sales
    for link in links:
        tree[link[0]].append(link[1])
    dfs(1)

    return min(dp[1])

print(solution(
[5, 6, 5, 3, 4], [[2,3], [1,4], [2,5], [1,2]]
))