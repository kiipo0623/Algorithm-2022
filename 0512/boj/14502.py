from itertools import combinations
from collections import deque
N, M = map(int, input().split())
board = []
virus = []
empty = []

answer = 0
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def checkout(row, col):
    if row<0 or col<0 or row>=N or col>=M:
        return True
    return False

def bfs(b):
    q = deque([])
    q.extend(virus)

    while q:
        now = q.popleft()
        for k in range(4):
            drow, dcol = now[0] + dx[k], now[1] + dy[k]
            if not checkout(drow, dcol) and b[drow][dcol] == 0:
                q.append((drow, dcol))
                b[drow][dcol] = 2
    s = 0
    for a in range(N):
        s += b[a].count(0)
    return s


def simulate(cand):
    tmp = [a[:] for a in board]
    for r, c in cand:
        tmp[r][c] = 1
    return bfs(tmp)

for i in range(N):
    data = list(map(int, input().split()))
    for j in range(M):
        if data[j] == 0:
            empty.append((i, j))
        elif data[j] == 2:
            virus.append((i, j))
    board.append(data)

candidate = list(combinations(empty, 3))
for cand in candidate:
    answer = max(simulate(cand), answer)

print(answer)