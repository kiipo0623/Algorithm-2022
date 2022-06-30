def bellman_ford(graph, N):
    for node in range(1, N+1):
        distance = [INF]*(N+1)
        distance[node] = 0

        for time in range(N): #V-1회 반복
            for mid in range(1, N+1):
                for finish in range(1, N+1):
                    if distance[finish] > distance[mid] + graph[mid][finish]:
                        if time == (N-1):
                            return "YES"
                        distance[finish] = distance[mid] + graph[mid][finish]
    return "NO"


TC = int(input())
INF = 10001
for _ in range(TC):
    N, M, W = map(int, input().split())
    graph = [[INF]*(N+1) for _ in range(N+1)]

    for _ in range(M):
        S, E, T = map(int, input().split())
        if graph[S][E] > T:
            graph[S][E] = T
        if graph[E][S] > T:
            graph[E][S] = T

    for _ in range(W):
        S, E, T = map(int, input().split())
        graph[S][E] = -(T)

    print(bellman_ford(graph, N))

