def dfs(root):
    global DP
    visited[root] = 1

    if len(graph[root]) == 0:
        DP[root][1] = 1
        DP[root][0] = 0

    for node in graph[root]:
        if not visited[node]:
            dfs(node)
            # 내가 아니면 자식들 전부 맞아야 함
            DP[root][0] += DP[node][1]
            DP[root][1] += min(DP[node][0], DP[node][1])
    DP[root][1] += 1



import sys
sys.setrecursionlimit(10**9)
input = sys.stdin.readline
N = int(input())
graph = [[] for _ in range(N+1)]
DP = [[0, 0] for _ in range(N+1)] # 0 얼리어답터아님 1얼리어답터임
visited = [0 for _ in range(N+1)]

for _ in range(N-1):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

dfs(1)
print(min(DP[1][0], DP[1][1]))