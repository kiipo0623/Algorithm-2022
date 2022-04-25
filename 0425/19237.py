# 0 : up / 1 : down / 2 : left / 3 : right
from copy import deepcopy
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
def find_shark(sharknum):
    for i in range(N):
        for j in range(N):
            if board[i][j] and board[i][j][0] == sharknum:
                return [i, j]
    return [-1, -1]

def make_smell():
    global smellboard
    for i in range(1, M+1):
        row, col = find_shark(i)
        if row == -1 and col == -1:
            continue
        smellboard[row][col] = [i, K]

def find_direct(nosmell, mysmell, sharknum, nowdirect):
    want_dir = direct_turn[sharknum][nowdirect]
    if len(nosmell):
        for d in want_dir:
            if d in nosmell:
                return d

    for d in want_dir:
        if d in mysmell:
            return d

def move_simul():
    global board
    newboard = [[False]*N for _ in range(N)]
    for i in range(1, M+1):
        row, col = find_shark(i)
        if row == -1 and col == -1: # 물고기 죽었으면
            continue
        nowdir = board[row][col][1]
        nosmell, mysmell = [], [] # 후보 방향 저장

        for k in range(4):
            drow, dcol = row + dx[k], col + dy[k]
            if 0<=drow<N and 0<=dcol<N:
                if smellboard[drow][dcol] == False:
                    nosmell.append(k)
                elif smellboard[drow][dcol][0] == i:
                    mysmell.append(k)

        newdir = find_direct(nosmell, mysmell, i, nowdir)
        nrow, ncol = row+dx[newdir], col+dy[newdir] # 이동

        if newboard[nrow][ncol]: # 살해
            if newboard[nrow][ncol][0] < i:
                continue
            else:
                newboard[nrow][ncol] = (i, newdir)
        else:
            newboard[nrow][ncol] = (i, newdir)
    board = deepcopy(newboard)

# def kill_shark(newboard):
#     for i in range(N):
#         for j in range(N):
#             if newboard[i][j] and len(newboard)>1:
#                 maxshark, sharkdir = -1, -1
#                 for s in newboard[i][j]:
#                     if s[0] > maxshark:
#                         maxshark, sharkdir = s[0], s[1]
#
#                 newboard[i][j] = [maxshark, sharkdir]
#     return newboard

def smell_update():
    global smellboard
    for i in range(N):
        for j in range(N):
            if smellboard[i][j]:
                smellboard[i][j][1] -= 1
                if smellboard[i][j][1] == 0:
                    smellboard[i][j] = False

def leave_shark():
    sharkcnt = 0
    for i in range(N):
        for j in range(N):
            if board[i][j]:
                sharkcnt += 1
                if sharkcnt > 1:
                    return False
    return True

def simulate():
    for i in range(1, 1001):
        # 이동 하기
        move_simul()
        # 냄새 시간 줄이기
        smell_update()
        # 자기자리에 냄새 뿌리기
        make_smell()

        # 체크
        # print("time", i)
        # print("board")
        # print(board)
        # print("smell")
        # print(smellboard)

        if leave_shark():
            return i

    return -1

N, M, K = map(int, input().split())
tmp = dict()
board = [[False]*N for _ in range(N)]
smellboard = [[False]*N for _ in range(N)]
direct_turn = dict()

for i in range(N):
    data = list(map(int, input().split()))
    for j in range(N):
        if data[j] != 0:
            tmp[data[j]] = (i, j)

direct = [0] + list(map(int, input().split()))

for i in range(1, M+1):
    shark_row, shark_col = tmp[i]
    sharkdir = direct[i]
    board[shark_row][shark_col] = (i, sharkdir-1)

for i in range(1, (M+1)):
    tmpdir = []
    for _ in range(4):
        data = list(map(int, input().split()))
        for j in range(4):
            data[j] = data[j]-1
        tmpdir.append(data)
    direct_turn[i] = tmpdir

make_smell()
print(simulate())



