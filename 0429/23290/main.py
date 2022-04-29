from collections import deque
from copy import deepcopy
direction = {1:(0, -1), 2:(-1, -1), 3:(-1, 0), 4:(-1, 1), 5:(0, 1), 6:(1, 1), 7:(1, 0), 8:(1, -1)}
dx = [0, -1, 0, 1, 0]
dy = [0, 0, -1, 0, 1]
def checkout(row, col):
    if row<0 or row>=4 or col<0 or col>=4:
        return True
    return False

def get_direct(row, col, dir):
    for i in range(8):
        drow, dcol = row+direction[dir][0], col+direction[dir][1]
        # 범위 내인지
        if checkout(drow, dcol):
            dir = dir-1
            if dir == 0:
                dir = 8
            continue
        # 상어 있는지
        if drow == sx and dcol == sy:
            dir = dir - 1
            if dir == 0:
                dir = 8
            continue
        # 냄새 있는지
        if smell[drow][dcol] > 0:
            dir = dir - 1
            if dir == 0:
                dir = 8
            continue

        return [True, drow, dcol, dir]

    return [False, row, col, dir]


def move_fish():
    global board
    newboard = [[deque([]) for _ in range(4)] for _ in range(4)]
    for i in range(4):
        for j in range(4):
            leng = len(board[i][j])
            for _ in range(leng):
                fishdir = board[i][j].popleft()
                next = get_direct(i, j, fishdir)
                newboard[next[1]][next[2]].append(next[3])
    board = deepcopy(newboard)

def shark_bt(r, c, dir, kill, fishboard):
    global shark_route_cand
    if len(dir) == 3:
        s = ''
        for i in range(3):
            s += str(dir[i])
        shark_route_cand.append((kill, s))
        return

    for k in range(1, 5):
        drow, dcol = r+dx[k], c+dy[k]
        if not checkout(drow, dcol):
            eatfish = fishboard[drow][dcol]
            dir.append(k)
            fishboard[drow][dcol] = 0
            shark_bt(drow, dcol, dir, kill+eatfish, fishboard)
            dir.pop()
            fishboard[drow][dcol] = eatfish

def fish_cnt():
    sum_ = 0
    fishboard =[[0]*4 for _ in range(4)]
    for i in range(4):
        for j in range(4):
            fishboard[i][j] = len(board[i][j])
            sum_ += fishboard[i][j]
    return fishboard, sum_

def shark_move():
    global sx, sy, board, smell
    fishboard = fish_cnt()[0]
    shark_bt(sx, sy, [], 0, fishboard)
    shark_route_cand.sort(key=lambda x: (-x[0], x[1]))
    route = shark_route_cand[0][1]
    for i in range(3):
        sdir = int(route[i])
        drow, dcol = sx+dx[sdir], sy+dy[sdir]
        if fishboard[drow][dcol] > 0:
            board[drow][dcol] = deque([])
            smell[drow][dcol] = 3
        sx, sy = drow, dcol

def delete_smell():
    global smell
    for i in range(4):
        for j in range(4):
            if smell[i][j]:
                smell[i][j] -= 1

def duplicate_magic(tmp):
    global board
    for i in range(4):
        for j in range(4):
            board[i][j].extend(tmp[i][j])

def simulate():
    global shark_route_cand
    for i in range(S):
        # 복제 마법
        duplicate = deepcopy(board)
        # 물고기 한 칸 이동
        move_fish()
        # 상어 연속 3칸 이동
        shark_move()
        shark_route_cand = [] # 초기화
        # 냄새 제거
        delete_smell()
        # 복제 마법
        duplicate_magic(duplicate)
        # print("i", i)
        # print("board")
        # print(board)
        # print("smell")
        # print(smell)
        # print("sx, sy ", sx, sy)

M, S = map(int, input().split())
board = [[deque([]) for _ in range(4)] for _ in range(4)]
smell = [[0]*4 for _ in range(4)]
shark_route_cand = []
for _ in range(M):
    fx, fy, d = map(int, input().split())
    board[fx-1][fy-1].append(d)
sx, sy = map(int, input().split())
sx, sy = sx-1, sy-1
simulate()
print(fish_cnt()[1])
