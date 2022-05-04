import heapq, math
INF = int(1e9)
def trap_check(now_pos, next_pos, now_state, trap_dict):
    now_trap_flag, next_trap_flag = False, False
    if now_pos in trap_dict: # 현재 위치의 트랩이 눌려있는지
        now_trap_flag = True if now_state & (1<<trap_dict[now_pos]) else False
    if next_pos in trap_dict:
        next_trap_flag = True if now_state & (1<<trap_dict[next_pos]) else False

    return now_trap_flag!=next_trap_flag # 다르면 눌려있는거임

def change_nextstate(next_pos, now_state, trap_dict):
    if next_pos in trap_dict:
        return now_state ^ (1<<trap_dict[next_pos])
    return now_state

def solution(n, start, end, roads, traps):
    answer = INF
    graph = [[] for _ in range(n+1)] # [도착지, cost, reverseFlag]
    trap_dict = {v:i for i, v in enumerate(traps)}
    # row = 현재 상태 col = 현재 방문 위치 sum을 저장
    cache = [[INF]*(n+1) for _ in range(int(math.pow(2, len(traps))))]

    for s, e, c in roads:
        graph[s].append([e, c, False])
        graph[e].append([s, c, True])

    cache[0][start] = 0
    hq = []
    heapq.heappush(hq, [0, start, 0]) # [sum, 현재위치, 현재상태]

    while hq:
        now_sum, now_pos, now_state = heapq.heappop(hq)
        if now_pos == end:
            answer = min(answer, now_sum)
            continue
        if now_sum > cache[now_state][now_pos]: # 등호 처리 어떻게 해야 하는지 : 첫 시작점 아니면 = 해도 되는데
            # 현재 위치에서 다음으로 가는 길을 갱신할 필요가 있냐 없냐 인데 현재 위치까지 가는 길이 같으면 솔직히 할 필요 없다
            continue

        for next_pos, next_cost, next_rev in graph[now_pos]: # 모든 것 가져옴
            # 갈 수 있는지 확인 : 현재rev상태와 트랩의 발동여부를 확인 : 트랩으로 들어오는거/트랩에서 나가는거
            if next_rev != trap_check(now_pos, next_pos, now_state, trap_dict): # 갈 수 없는 경우
                continue
            cost = now_sum + next_cost
            # 다음 상태 : 새로 도착하는 곳의 flag 갱신
            next_state = change_nextstate(next_pos, now_state, trap_dict)

            if cost >= cache[next_state][next_pos]:
                continue

            cache[next_state][next_pos] = cost
            heapq.heappush(hq, [cost, next_pos, next_state])

    return answer

print(solution(
    4, 1, 4,[[1, 2, 1], [3, 2, 1], [2, 4, 1]], [2, 3]
))