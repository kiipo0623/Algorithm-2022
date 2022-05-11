def checkout(row, col):
    global L
    if row<0 or col<0 or row>(L+1) or col>(L+1):
        return True
    return False

from collections import deque
dx = [1, 0]
dy = [0, 1]

def bfs(row, col, problems):
    global time, L
    queue = deque()
    queue.append((row, col))
    visited = [[False]*(L+2) for _ in range(L+2)]

    for i in range(row+1):
        for j in range(col+1):
            visited[i][j] = True

    while queue:
        a, c = queue.popleft()
        if visited[a][c] == True:
            continue
        visited[a][c]= True
        for p in problems:
            alp_req, cop_req, alp_rwd, cop_rwd, cost = p
            if (a - alp_rwd >= alp_req and c - cop_rwd >= cop_req) and (a - alp_rwd >= row and c - cop_rwd >= col):
                time[a][c] = min(time[a][c], time[a - alp_rwd][c - cop_rwd] + cost)
        for k in range(2):
            da, dc = a+dx[k], c+dy[k]
            if not checkout(da, dc) and not visited[da][dc]:
                queue.append((da, dc))
    print(visited)

def solution(alp, cop, problems):
    global time, L
    MAX_ALP, MAX_COP = 0, 0
    for p in problems:
        if p[0] > MAX_ALP:
            MAX_ALP = p[0]
        if p[1] > MAX_COP:
            MAX_COP = p[1]

    L = max(MAX_ALP, MAX_COP)

    time = [[0] * (L+2) for _ in range(L+2)]

    for i in range(L+2):
        for j in range(L+2):
            if checkout(alp + i, cop + j):
                continue
            time[alp + i][cop + j] = i + j

    bfs(alp, cop, problems)
    print(time)

    return time[MAX_ALP][MAX_COP]



print(solution(
    10, 10, [[10,15,2,1,2],[20,20,3,3,4]]
))
# print(solution(
#     0, 0, [[0,0,2,1,2],[4,5,3,1,2],[4,11,4,0,2],[10,4,0,4,2]]
# ))