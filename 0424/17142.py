from collections import deque
from copy import deepcopy
def combi(lst, cnt, M):
    global candidate

    if cnt == M:
        candidate.append(lst[:])
        return

    start = virus.index(lst[-1])+1 if lst else 0
    for i in range(start, len(virus)):
        lst.append(virus[i])
        combi(lst, cnt+1, M)
        lst.pop()

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def simulate(cand, board, emptycnt):
    b = deepcopy(board)
    for row, col in cand:
        b[row][col] = 0

    maxcnt = 0
    queue = deque(cand)
    while queue:
        if emptycnt == 0:
            return maxcnt

        row, col = queue.popleft()
        for i in range(4):
            drow, dcol = row+dx[i], col+dy[i]
            if 0<=drow<N and 0<=dcol<N:
                if b[drow][dcol] == 'N' or b[drow][dcol] == 'F':
                    if b[drow][dcol] == 'N':
                        emptycnt -= 1
                    b[drow][dcol] = b[row][col]+1
                    maxcnt = max(maxcnt, b[drow][dcol])
                    queue.append((drow, dcol))

    if emptycnt == 0:
        return maxcnt
    else:
        return int(1e9)




N, M = map(int, input().split())
virus = []
candidate = []
board = []
emptycnt = 0
mintime = int(1e9)
for i in range(N):
    data = list(map(int, input().split()))
    for j in range(N):
        if data[j] == 0:
            emptycnt += 1
            data[j] = 'N'
        elif data[j] == 1:
            data[j] = 'W'
        elif data[j] == 2:
            data[j] = 'F'
            virus.append((i, j))
    board.append(data)

combi([], 0, M)
for cand in candidate:
    mintime = min(mintime, simulate(cand, board, emptycnt))
if mintime == int(1e9):
    print(-1)
else:
    print(mintime)