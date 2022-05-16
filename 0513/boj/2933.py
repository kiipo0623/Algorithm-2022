from collections import deque
# 클러스터가 여러개가 되는 경우 미고려 ! ㅆㅂ
R, C = map(int, input().split())
board = []
for _ in range(R):
    board.append(list(input()))
board.append(['x']*C)
N = int(input())
fight = list(map(int, input().split()))

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def checkout(row, col):
    if row<0 or col<0 or row>=(R+1) or col>=C:
        return True
    return False

def bfs():
    tmp = [a[:] for a in board]
    queue = deque([])
    queue.append((R, 0))
    tmp[R][0] = 'o'

    while queue:
        row, col = queue.popleft()
        for k in range(4):
            drow, dcol = row + dx[k] , col + dy[k]
            if not checkout(drow, dcol) and tmp[drow][dcol] == 'x':
                tmp[drow][dcol] = 'o'
                queue.append((drow, dcol))

    for i in range(R+1):
        if 'x' in tmp[i]:
            return [True, tmp]
    return [False, tmp]

def find_cluster_bfs(r, c, b):
    queue = deque()
    queue.append((r, c))
    b[r][c] = 'c'

    while queue:
        row, col = queue.popleft()
        for k in range(4):
            drow, dcol = row+dx[k], col+dy[k]
            if not checkout(drow, dcol) and b[drow][dcol] == 'x':
                b[drow][dcol] = 'c'
                queue.append('c')
    return b


def find_cluster(b):
    for i in range(R+1):
        for j in range(C):
            if b[i][j] == 'x':
                new_b = find_cluster_bfs(i, j, b)
                return new_b
    return False # 더이상 없음

def fall_check(b):
    DIS = R+2
    mv_col = []
    for i in range(C):
        flag, cnt = False, 0
        for j in range(R+1):
            if not flag and b[j][i] == 'c':
                flag = True
            if flag and b[j][i] == '.':
                cnt += 1
            if flag and b[j][i] == 'o':
                break
        if flag:
            mv_col.append(i)
            if DIS > cnt: DIS = cnt
    return [DIS, mv_col]

def move_board(move_cnt, move_col, tmp):
    for col in move_col:
        for row in range(R, -1, -1):
            if tmp[row][col] == 'x':
                board[row+move_cnt][col] = 'x' # 찜찜
                board[row][col] = '.'


for i in range(N):
    if i%2 == 0: # 왼쪽에서 오른쪽
        for j in range(0, C):
            if board[R-fight[i]][j] == 'x':
                board[R-fight[i]][j] = '.'
                break

    elif i%2 == 1: # 오른쪽에서 왼쪽
        for j in range(C-1, -1, -1):
            if board[R-fight[i]][j] == 'x':
                board[R-fight[i]][j] = '.'
                break
    # 떠있는지 확인
    flag, b = bfs()
    if flag: # 떠있다
        # 모든 존재에 대해서 bfs 진행 :
        while find_cluster(b):
            # 제일 높은 곳 확인(x에 대해서): row별로 탐색해서 if x : row 차이가 가장 작은 곳 리턴
            mv_cnt, mv_col = fall_check(b)
            # 이동 : 진짜 board에다가
            move_board(mv_cnt, mv_col, b)
    else: # 안떠있다
        continue
for i in range(R):
    print(''.join(board[i]))