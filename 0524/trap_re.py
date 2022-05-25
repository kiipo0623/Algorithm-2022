import heapq, math
INF = int(1e9)
def check_flag(now_pos, next_pos, now_state, trap_dict):
    now_flag, next_flag = False, False
    if now_pos in trap_dict:
        if now_state & (1<<trap_dict[now_pos]):
            now_flag = True

    if next_pos in trap_dict:
        if now_state & (1<<trap_dict[next_pos]):
            next_flag = True
    return now_flag != next_flag

def change_state(next_pos, now_state, trap_dict):
    if next_pos in trap_dict:
        return now_state ^ (1<<trap_dict[next_pos])
    return now_state

def solution(n, start, end, roads, traps):
    answer = INF
    graph = [[] for _ in range(n+1)]

    for p, q, s in roads:
        graph[p].append([q, s, False]) # 도착지 비용 화살표방향
        graph[q].append([p, s, True])

    trap_dict = {v:i for i, v in enumerate(traps)}
    cache = [[INF]*(n+1) for _ in range(int(math.pow(2, len(traps))))]

    hq = []
    cache[0][start] = 0
    heapq.heappush(hq, [0, start, 0]) # distance, now, state

    while hq:
        dist, now_pos, now_state = heapq.heappop(hq)
        if now_pos == end:
            answer = min(answer, dist)
            continue

        if cache[now_state][now_pos] < dist:
            continue

        for next_pos, cost, flag in graph[now_pos]:
            if flag == check_flag(now_pos, next_pos, now_state, trap_dict):
                next_state = change_state(next_pos, now_state, trap_dict)
                if cache[next_state][next_pos] > dist + cost:
                    cache[next_state][next_pos] = dist + cost
                    heapq.heappush(hq, [dist+cost, next_pos, next_state])

    return answer

print(solution(3, 1, 3, [[1,2,2],[3,2,3]], [2]))