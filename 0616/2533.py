def treedp(start):
    global DP, visited, graph
    visited[start] = 1
    if len(graph[start]) == 0:
        DP[start][1] = 1
        DP[start][0] = 0

    else:
        for i in graph[start]:
            if visited[i] == 0:
                treedp(i)
                DP[start][1] += min(DP[i][0], DP[i][1])
                DP[start][0] += DP[i][1]
        DP[start][1] += 1


N = int(input())
graph = [[] for _ in range(N+1)]
DP = [[0, 0] for _ in range(N+1)]

for _ in range(N-1):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

visited = [0 for i in range(N+1)]
treedp(1)
print(min(DP[1][0], DP[1][1]))
