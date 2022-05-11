from collections import deque
dx = [1, 0]
dy = [0, 1]
# 서로 종속적인 관계를 가진다는 것을 고려해야 합니다. 그러나 해당 코드는 고려되지 않아 오답이 발생합니다
def checkout(row, col):
    global L
    if row<0 or col<0 or row>=L+2 or col>=L+2:
        return True
    return False

def bfs(alp, cop, problems):
    global L, time
    visited = [[False]*(L+2) for _ in range(L+2)]
    queue = deque([])
    queue.append((alp, cop))

    while queue:
        now_alp, now_cop = queue.popleft()
        print(now_alp, now_cop)
        if not visited[now_alp][now_cop]:
            visited[now_alp][now_cop] = True
            for p in problems:
                alp_req, cop_req, alp_rwd, cop_rwd, cost = p
                if (now_alp - alp_rwd >= alp_req and now_cop - cop_rwd >= cop_req) and (now_alp-alp_rwd >= alp and now_cop - cop_rwd >= cop):
                    if time[now_alp-alp_rwd][now_cop-cop_rwd]+cost < time[now_alp][now_cop]:
                        time[now_alp][now_cop] = time[now_alp-alp_rwd][now_cop-cop_rwd]+cost
                        if not checkout(now_alp, now_cop+1):
                            time[now_alp][now_cop+1] = min(time[now_alp][now_cop+1], time[now_alp][now_cop]+1)
                        if not checkout(now_alp+1, now_cop):
                            time[now_alp+1][now_cop] = min(time[now_alp+1][now_cop], time[now_alp][now_cop]+1)
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
    10, 10, [[10,15,2,1,2],[20,20,3,3,4]]
))