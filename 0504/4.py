import sys
sys.setrecursionlimit(10000)
INF = int(1e9)
# 비용 이동횟수 현재위치
def bt(time, cnt, now, graph, traps, maxcnt, end, n):
    global answer
    if now == end:
        answer = min(answer, time)
        return

    if cnt == maxcnt: # 매 턴의 최종
        return

    for i in range(1, n+1):
        if graph[now][i] != INF: # 갈 수 있는 길이면 간다!
            # 이동 하고 트랩 바뀜
            cost, new = graph[now][i], i
            tmp = [a[:] for a in graph]
            # 트랩 처리 : 뒤집기
            if new in traps:
                for k in range(1, n+1):
                    tmp[new][k], tmp[k][new] = tmp[k][new], tmp[new][k]
            bt(time+cost, cnt+1, new, tmp, traps, maxcnt, end, n)


def solution(n, start, end, roads, traps):
    global answer
    answer = INF
    graph = [[INF]*(n+1) for _ in range(n+1)]

    for road in roads:
        P, Q, S = road
        graph[P][Q] = S

    fin = 1
    while True:
        bt(0, 0, start, graph, traps, fin, end, n)
        if answer != INF:
            break
        fin += 1
    return answer

# print(solution(
#     3, 1, 3, [[1, 2, 2], [3, 2, 3]], [2]
# ))
print(solution(
    4, 1, 4, [[1, 2, 1], [3, 2, 1], [2, 4, 1]], [2, 3]
))