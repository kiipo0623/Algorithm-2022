def solution(n, s, a, b, fares):
    answer = 0
    INF = int(1e9)
    graph = [[INF for _ in range(n+1)] for _ in range(n+1)]
    for fare in fares:
        c, d, f = fare
        graph[c][d] = f
        graph[d][c] = f

    for k in range(1, n+1):
        graph[k][k] = 0
        for x in range(1, n+1):
            for y in range(1, n+1):
                graph[x][y] = min(graph[x][y], graph[x][k]+graph[k][y])

    mincost = graph[s][a] + graph[s][b]
    for k in range(1, n+1):
        mincost = min(mincost, graph[s][k]+graph[k][a]+graph[k][b])

    return mincost

print(solution(
    6, 4, 6, 2, [[4, 1, 10], [3, 5, 24], [5, 6, 2], [3, 1, 41], [5, 1, 24], [4, 6, 50], [2, 4, 66], [2, 3, 22], [1, 6, 25]]
))