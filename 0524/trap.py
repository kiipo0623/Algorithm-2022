import heapq, math
INF = int(1e9)

def trap_check(now_pos, next_pos, now_state, trap_dict):
    now_trap_flag, next_trap_flag = False, False
    if now_pos in trap_dict: # 내가 트랩이면
        now_trap_flag = True if now_state & (1<<trap_dict[now_pos]) else False
    if next_pos in trap_dict: # 다음이 트랩이면
        next_trap_flag = True if now_state & (1<<trap_dict[next_pos]) else False
    return now_trap_flag != next_trap_flag

def change_nextstate(next_pos, now_state, trap_dict):
    if next_pos in trap_dict:
        return now_state ^ (1<<trap_dict[next_pos])
    return now_state

def solution(n, start, end, roads, traps):
    answer = INF
    graph = [[] for _ in range(n+1)] # 도착지, cost revFlag
    # node마다 뒤집혓는지 표시
    trap_dict = {v:i for i, v in enumerate(traps)}
    # row : 현재 상태
    # col : 현재 방문 위치 sum
    # 트랩 뭐뭐 눌렸을 때 최소 값 : 다익이 이전에 탐색한 최솟값 가지고 진행하니까
    cache = [[INF]*(n+1) for _ in range(int(math.pow(2, len(traps))))]

    for s, e, c in roads:
        graph[s].append([e, c, False])
        graph[e].append([s, c, True])

    cache[0][start] = 0
    hq = []
    heapq.heappush(hq, [0, start, 0]) # [sum, 현재위치, 현재상태]

    while hq:
        now_sum, now_pos, now_state = heapq.heappop(hq)
        if now_pos == end: # 성공
            answer = min(answer, now_sum)
            continue
        if now_sum > cache[now_state][now_pos]: # 다익의 과정
            continue
        for next_pos, next_cost, next_rev in graph[now_pos]:
            if next_rev != trap_check(now_pos, next_pos, now_state, trap_dict):
                continue
            cost = now_sum + next_cost
            next_state = change_nextstate(next_pos, now_state, trap_dict)
            if cost >= cache[next_state][next_pos]:
                continue
            cache[next_state][next_pos] = cost
            heapq.heappush(hq, [cost, next_pos, next_state])
    return answer