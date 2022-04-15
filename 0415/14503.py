# 로봇 청소기

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

def turn_left(d):
    # if d == 0:
    #     d = 3
    # elif d == 3 or d == 2 or d == 1:
    #     d -= 1
    d = (d+3)%4

    return d

def back(d):
    # if d == 0:
    #     d == 2
    # elif d == 1:
    #     d == 3
    # elif d == 2:
    #     d == 0
    # elif d == 3:
    #     d == 1
    d = (d+2)%4

    return d

def simulation(graph, row, col, dir, N, M):
    if graph[row][col] == 0:
        graph[row][col] = 2

    for i in range(4):
        dir = turn_left(dir)
        nrow, ncol = row+dx[dir], col+dy[dir]
        if 0<=nrow<N and 0<=ncol<M and graph[nrow][ncol] == 0:
            return simulation(graph, nrow, ncol, dir, N, M)

    new_dir = back(dir)
    nrow, ncol = row+dx[new_dir], col+dy[new_dir]
    if graph[nrow][ncol] == 1:
        return
    else:
        return simulation(graph, nrow, ncol, dir, N, M)

import sys
input = sys.stdin.readline

N, M = map(int, input().split())
r, c, d = map(int, input().split())
graph = []
for _ in range(N):
    graph.append(list(map(int, input().split())))

simulation(graph, r, c, d, N, M)
ans = 0

for i in range(N):
    ans += graph[i].count(2)

print(ans)

