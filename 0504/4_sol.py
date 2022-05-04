import heapq
INF = int(1e9)

# 갈 수 있는 방향 판별 함수
# 현재위치 다음위치 현재상태(그래프) 트랩인덱스
def isReverse(cur_pos, next_pos, cur_state, traps_idx):
    is_cur_trap_on, is_next_trap_on = False, False
    if cur_pos in traps_idx: # 지금 내 위치가 트랩 위
        is_cur_trap_on = (cur_state & (1<<traps_idx[cur_pos])) > 0 # 현재 트랩이 발동된 상태인지(그래프가 뒤집힌)
    if next_pos in traps_idx:
        is_next_trap_on = (cur_state & (1 << traps_idx[next_pos])) > 0 # 다음 트랩이 발돈된 상태인지
    # (T, T) : False(둘 다 발동) 해당 edge가 원래 방향임
    # (T, F), (F, T) : True(하나만 발동) 해당 edge가 뒤집힌 방향임
    # (F, F) : False(둘 다 안발동) 해당 edge가 원래 방향임
    return is_cur_trap_on != is_next_trap_on

# 새로 가는 곳이 함정이면 비트 토글
def getNextState(next_pos, cur_state, traps_idx):
    if next_pos in traps_idx:
        return cur_state ^ (1 << traps_idx[next_pos])
    return cur_state

def solution(n, start, end, roads, traps):
    answer = INF
    # 최단 거리 리스트 : 그래프 상황(어떤 트랩이 발동했는지)에 따라 다르다
    # row = 그래프 상황  col = 현재 노드
    min_cost = [[INF for _ in range(n+1)] for _ in range(2**len(traps))]
    # 트랩 번호 : 트랩리스트의 인덱스
    traps_idx = {v: i for i, v in enumerate(traps)} #0번 인덱스에 해당하는 트랩(실제번호)가 발동하면 원래 인덱스로 뒤집어서 min_cost 작게 제작
    # 연결 리스트
    graph = [[] for _ in range(n+1)] # end cost isReverse

    # 그래프 생성
    for _s, _e, _c in roads:
        graph[_s].append([_e, _c, False])
        graph[_e].append([_s, _c, True])

    hq = [] # sum cur_pos, trap_state
    heapq.heappush(hq, [0, start, 0])
    min_cost[0][start] = 0 # 첫 시작점

    while hq:
        cur_sum, cur_pos, cur_state = heapq.heappop(hq)
        if cur_pos == end: # 만약 도착했으면
            answer = min(answer, cur_sum)
            continue
        if cur_sum > min_cost[cur_state][cur_pos]: # 이미 갱신된 것
            continue
        for next_pos, next_cost, is_reverse in graph[cur_pos]:
            # 못 가는 방향이면 pass : 트랩 때문에 뒤집혀서 가는 길이 사라지는 경우?
            if is_reverse != isReverse(cur_pos, next_pos, cur_state, traps_idx): # 트랩이 반대인 경우 원래 길로 갈 수 없음
                continue

            next_state = getNextState(next_pos, cur_state, traps_idx)
            next_sum = next_cost + cur_sum

            if next_sum >= min_cost[next_state][next_pos]:
                continue

            min_cost[next_state][next_pos] = next_sum
            heapq.heappush(hq, [next_sum, next_pos, next_state])
    return answer

print(solution(
    4, 1, 4, [[1, 2, 1], [3, 2, 1], [2, 4, 1]], [2, 3]
))