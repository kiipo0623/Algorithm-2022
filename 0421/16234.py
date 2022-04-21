from copy import deepcopy
from collections import deque

drow = [-1, 1, 0, 0]
dcol = [0, 0, -1, 1]

def bfs(row, col, visit, new_g, g):
    queue = deque()
    queue.append((row, col))

    checker = [[False]*N for _ in range(N)]
    checker[row][col], visit[row][col] = True, True
    sum_, cnt_ = g[row][col], 1

    while queue:
        nrow, ncol = queue.popleft()
        for i in range(4):
            arow, acol = nrow+drow[i], ncol+dcol[i]
            if 0<=arow<N and 0<=acol<N and checker[arow][acol] == False:
                if L<=abs(g[nrow][ncol]-g[arow][acol])<=R:
                    checker[arow][acol], visit[arow][acol] = True, True
                    sum_ += g[arow][acol]
                    cnt_ += 1
                    queue.append((arow, acol))

    one = sum_//cnt_
    for i in range(N):
        for j in range(N):
            if checker[i][j] == True:
                new_g[i][j] = one
    return new_g


def check_boundary(g):
    new_g = deepcopy(g)
    visit = [[False]*N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            if visit[i][j] == False:
                new_g = bfs(i, j, visit, new_g, g)
    return new_g

def simulation():
    before = deepcopy(graph)
    counter = 0
    while True:
        after = check_boundary(deepcopy(before))
        if before == after:
            return counter
        else:
            before = deepcopy(after)
            counter += 1


N, L, R = map(int, input().split())
graph = []
for _ in range(N):
    graph.append(list(map(int, input().split())))
print(simulation())
