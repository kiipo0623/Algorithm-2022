# 삼성 기출 연구소
import sys
from itertools import combinations
from copy import deepcopy

def exceptwall(candidate, graph, M):
    real_cand = []
    for c in candidate:
        if graph[c//M][c%M] == 0:
            real_cand.append([c//M, c%M])
    return real_cand

def makewall(candidate):
    return list(map(list, combinations(candidate, 3)))

def checkwall(walllist, graph, N):
    coordinate = []
    for item in walllist:
        row = item//M
        col = item%M
        if graph[row][col] != 0:
            return [False, []]
        else:
            coordinate.append([row, col])
    return [True, coordinate]

def virus_coord(graph):
    virus = []
    for i in range(N):
        for j in range(M):
            if graph[i][j] == 2:
                virus.append([i, j])
    return virus

def dfs(coordinate, graph, virus, N):
    ans = 0
    for row, col in coordinate:
        graph[row][col] = 1
    stack = []
    stack.extend(virus)

    dx = [0, 0, -1, 1]
    dy = [-1, 1, 0, 0]

    while stack:
        nrow, ncol = stack.pop()
        for i in range(4):
            drow, dcol = nrow+dx[i], ncol+dy[i]
            if 0<=drow<N and 0<=dcol<M and graph[drow][dcol] == 0:
                graph[drow][dcol] = 2
                stack.append([drow, dcol])

    for i in range(N):
        ans += graph[i].count(0)
    return ans


input = sys.stdin.readline

N, M = map(int, input().split())
graph = []
for _ in range(N):
    graph.append(list(map(int, input().split())))

FULL = N*M
candidate = [i for i in range(FULL)]
realcand = exceptwall(candidate, graph, M)

wall_cand = makewall(realcand)
virus = virus_coord(graph)
max_ = 0

for wall in wall_cand:
    max_ = max(max_, dfs(wall, deepcopy(graph), virus, N))

print(max_)