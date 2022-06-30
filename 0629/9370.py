# 애초에 문제를 잘못읽은 셈 !
# g, h 를 지나가는 게 최단거리인 경우만 선택
import heapq
def dijkstra(s):
    h = []
    distance = [INF] * (n+1)
    distance[s] = 0
    heapq.heappush(h, (0, s))

    # distance라는 게 현재 최선의 길 : 갱신하면 그 길로가지말고 이 길로가는게어때?
    while h:
        dist, now = heapq.heappop(h)
        # now를 거쳐서 가라는 뜻
        for node, nodedis in graph[now]:
            update = dist + nodedis
            if distance[node] > update:
                distance[node] = update
                heapq.heappush(h, (update, node))
    return distance


TC = int(input())
INF = int(1e9)
for _ in range(TC):
    n, m, t = map(int, input().split())
    s, g, h = map(int, input().split())
    hg = 0
    graph = [[] for _ in range(n+1)]
    target = []
    answer = []
    for _ in range(m):
        a, b, d = map(int, input().split())
        if (a, b) == (g, h) or (a, b) == (h, g):
            hg = d
        graph[a].append((b, d))
        graph[b].append((a, d))
    for _ in range(t):
        target.append(int(input()))
    start_dist = dijkstra(s)
    g_dist = dijkstra(g)
    h_dist = dijkstra(h)
    for t in target:
        g_min = start_dist[h] + hg + g_dist[t]
        h_min = start_dist[g] + hg + h_dist[t]
        if start_dist[t] == min(g_min, h_min):
            answer.append(t)

    print(' '.join(map(str, list(sorted(answer)))))