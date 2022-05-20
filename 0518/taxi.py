import heapq
def dijkstra(start, n):
    global graph
    distance = [float('inf')]*(n+1)
    distance[start] = 0
    h = []
    distance[start] = 0
    heapq.heappush(h, (0, start))

    while h:
        dist, now = heapq.heappop(h)
        if distance[now] < dist:
            continue
        for node, cost in graph[now]:
            if distance[node] > cost + dist:
                distance[node] = cost+dist
                heapq.heappush(h, (cost+dist, node))

    return distance

    pass
def solution(n, s, a, b, fares):
    global graph
    graph = [[] for _ in range(n+1)]
    for fare in fares:
        c, d, f = fare
        graph[c].append((d, f))
        graph[d].append((c, f))

    # s에서 출발하는거 구하기 > a+b를 default로
    ston = dijkstra(s, n)
    answer = ston[a]+ston[b]
    # 모든 위치에 대해서 다시 다익스트라
    for node in range(1, n+1):
        distance = dijkstra(node, n)
        answer = min(answer, ston[node]+distance[a]+distance[b])
    return answer

print(solution(
    # 6,4,6,2,[[4, 1, 10], [3, 5, 24], [5, 6, 2], [3, 1, 41], [5, 1, 24], [4, 6, 50], [2, 4, 66], [2, 3, 22], [1, 6, 25]]
    # 7,3,4,1,[[5, 7, 9], [4, 6, 4], [3, 6, 1], [3, 2, 3], [2, 1, 6]]
    # 6,4,5,6,
))