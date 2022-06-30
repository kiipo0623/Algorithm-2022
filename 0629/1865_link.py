def bellman_ford(graph, N):
    node = 0
    distance = [INF]*(N+1)
    distance[node] = 1

    for time in range(N):
        for mid in graph:
            for finish in graph[mid]:
                if distance[finish] > distance[mid] + graph[mid][finish]:
                    if time == (N-1):
                        return "YES"
                    distance[finish] = distance[mid] + graph[mid][finish]
    return "NO"


TC = int(input())
INF = 10001
for _ in range(TC):
    N, M, W = map(int, input().split())
    graph = {i:{} for i in range(1, N+1)}

    for _ in range(M):
        S, E, T = map(int, input().split())
        if not graph[S].get(E) or graph[S][E] > T:
            graph[S][E] = T
        if not graph[E].get(S) or graph[E][S] > T:
            graph[E][S] = T

    for _ in range(W):
        S, E, T = map(int, input().split())
        graph[S][E] = -(T)

    print(bellman_ford(graph, N))

