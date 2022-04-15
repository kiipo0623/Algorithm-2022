# 로봇 청소기

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]


def simulation(graph, row, col, dir, N, M):
    if graph[row][col] == 0:
        graph[row][col] = 2

    for i in range(4):
        ndir = (dir + 3) % 4
        nrow, ncol = row+dx[ndir], col+dy[ndir]
        if 0<=nrow<N and 0<=ncol<M and graph[nrow][ncol] == 0:
            return simulation(graph, nrow, ncol, ndir, N, M)
        dir = ndir

    new_dir = (dir + 2) % 4
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

print(graph)
print(ans)

