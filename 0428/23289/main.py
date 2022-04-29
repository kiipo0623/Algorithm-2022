from collections import deque
from math import floor

# RIGHT LEFT UP DOWN
heatgo = {1: [(-1, 1), (0, 1), (1, 1)], 2: [(-1, -1), (0, -1), (1, -1)], 3: [(-1, -1), (-1, 0), (-1, 1)],
          4: [(1, -1), (1, 0), (1, 1)]}
cannotgoRIGHT = {(-1, 1): [(0, 0, 0), (-1, 0, 1)], (0, 1): [(0, 0, 1)], (1, 1): [(1, 0, 0), (1, 0, 1)]}  # 오른쪽 기준
cannotgoLEFT = {(-1, -1): [(0, 0, 0), (-1, -1, 1)], (0, -1): [(0, -1, 1)], (1, -1): [(1, 0, 0), (1, -1, 1)]}  # 왼쪽 기준
cannotgoUP = {(-1, -1): [(0, -1, 0), (0, -1, 1)], (-1, 0): [(0, 0, 0)], (-1, 1): [(0, 1, 0), (0, 0, 1)]}
cannotgoDOWN = {(1, -1): [(1, -1, 0), (0, -1, 1)], (1, 0): [(1, 0, 0)], (1, 1): [(1, 1, 0), (0, 0, 1)]}  # 아래쪽 기준
# 오른쪽 왼쪽 위 아래
dr = [0, 0, 0, -1, 1]
dc = [0, 1, -1, 0, 0]


def check_go(row, col, dir):  # 해당 방향으로 이동할 수 있는지 (범위, 벽 체크)
    update = []
    go_cand = heatgo[dir]
    if dir == 1:
        not_cand = cannotgoRIGHT
    elif dir == 2:
        not_cand = cannotgoLEFT
    elif dir == 3:
        not_cand = cannotgoUP
    elif dir == 4:
        not_cand = cannotgoDOWN

    for i in range(3):
        flag = True
        drow, dcol = row + go_cand[i][0], col + go_cand[i][1]
        for w in not_cand[(go_cand[i][0], go_cand[i][1])]:
            wrow, wcol = row + w[0], col + w[1]
            if (wrow, wcol, w[2]) in wall:
                flag = False
                break
        if not flag:
            continue
        if drow<0 or drow>=R or dcol<0 or dcol>=C:
            continue

        update.append((drow, dcol))
    return update

def checkout(row, col):
    if row<0 or row>=R or col<0 or col>=C:
        return True
    return False

def update_heat(r, c, dir): # 온풍기 바람 총괄
    global board
    tmp = [[0] * C for _ in range(R)]
    queue = deque([])
    drow, dcol = r + dr[dir], c + dc[dir]
    tmp[drow][dcol] = 5
    queue.append((drow, dcol, 5))

    while queue:
        row, col, heat = queue.popleft()
        if heat > 1:
            ud = check_go(row, col, dir)
            for u in ud:
                tmp[u[0]][u[1]] = heat-1
                queue.append((u[0], u[1], heat-1))

    for i in range(R):
        for j in range(C):
            board[i][j] += tmp[i][j]


def coord_heat():
    change = [[0]*C for _ in range(R)]
    checkdir = [(-1, 0), (0, 1)]
    for i in range(R):
        for j in range(C):
            for k in range(2):
                drow, dcol = i + checkdir[k][0], j + checkdir[k][1]
                if not checkout(drow, dcol) and (i, j, k) not in wall: # 범위 안에 있으면
                    diff = abs(board[i][j] - board[drow][dcol])
                    diff = floor(diff/4)
                    if board[i][j] > board[drow][dcol]:
                        change[i][j] -= diff
                        change[drow][dcol] += diff
                    elif board[i][j] < board[drow][dcol]:
                        change[i][j] += diff
                        change[drow][dcol] -= diff

    for i in range(R):
        for j in range(C):
            board[i][j] += change[i][j]

def outer_heat():
    if board[0][0] > 0:
        board[0][0] -= 1

    if board[R-1][0] > 0:
        board[R-1][0] -= 1

    if board[0][C-1] > 0:
        board[0][C-1] -= 1

    if board[R-1][C-1] > 0:
        board[R-1][C-1] -= 1

    for i in range(1, R-1):
        if board[i][0] > 0:
            board[i][0] -= 1
        if board[i][C-1] > 0:
            board[i][C-1] -= 1

    for i in range(1, C-1):
        if board[0][i] > 0:
            board[0][i] -= 1
        if board[R-1][i] > 0:
            board[R-1][i] -= 1

def simulate():
    global chocolate
    while True:
        if chocolate > 100:
            return
        # 각 히터마다 확산 조사 후 board 업데이트
        for h in heater:
            update_heat(h[0], h[1], h[2])
        # 온도 조절
        coord_heat()
        # 바깥쪽 온도 감소
        outer_heat()
        # 초콜릿 update
        chocolate += 1

        # K개 위치 조사
        kcnt = 0
        for r, c in checker:
            if board[r][c] >= K:
                kcnt += 1
        if kcnt == len(checker):
            return


R, C, K = map(int, input().split())
board = [[0] * C for _ in range(R)]
wall = []
heater = []
checker = []
chocolate = 0
for i in range(R):
    data = list(map(int, input().split()))
    for j in range(C):
        if data[j] in [1, 2, 3, 4]:
            heater.append((i, j, data[j]))
        elif data[j] == 5:
            checker.append((i, j))
W = int(input())
for _ in range(W):
    x, y, t = map(int, input().split())
    x, y = x-1, y-1
    wall.append((x, y, t))
simulate()
print(chocolate)

