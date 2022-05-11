from collections import deque
dx = [1, 0]
dy = [0, 1]
def bfs(alp, cop, problems):
    global L, time
    visited = [[False]*(L+2) for _ in range(L+2)]
    queue = deque([])
    queue.append((alp, cop))

    while queue:
        now_alp, now_cop = queue.popleft()
        if not visited[now_alp][now_cop]:
            visited[now_alp][now_cop] = True
            for p in problems:
                alp_req, cop_req, alp_rwd, cop_rwd, cost = p
                if (now_alp - alp_rwd >= alp_req and now_cop - cop_rwd >= cop_req) and (now_alp-alp_rwd >= alp and now_cop - cop_rwd >= cop):
                    time[now_alp][now_cop] = min(time[now_alp-alp_rwd][now_cop-cop_rwd]+cost, time[now_alp][now_cop])
            for k in range(2):
                next_alp, next_cop = now_alp+dx[k], now_cop+dy[k]
                if not checkout(next_alp, next_cop) and not visited[next_alp][next_cop]:
                    queue.append((next_alp, next_cop))

def checkout(row, col):
    if row<0 or col<0 or row>=(L+2) or col>=(L+2):
        return True
    return False

def solution(alp, cop, problems):
    global L, time
    answer = 0
    MAX_ALP, MAX_COP = 0, 0
    for p in problems:
        if p[0]>MAX_ALP:
            MAX_ALP = p[0]
        if p[1]>MAX_COP:
            MAX_COP = p[1]
    L = max(MAX_ALP, MAX_COP)

    time = [[0]*(L+2) for _ in range(L+2)]

    for i in range(L+2):
        for j in range(L+2):
            if not checkout(i+alp, j+cop):
                time[i+alp][j+cop] = (i+j)

    bfs(alp, cop, problems)

    return time[MAX_ALP][MAX_COP]

print(solution(
    0, 0, [[0,0,2,1,2],[4,5,3,1,2],[4,11,4,0,2],[10,4,0,4,2]]
))