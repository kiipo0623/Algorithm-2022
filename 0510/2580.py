import sys
input = sys.stdin.readline

def check(zeroidx, number, board):
    row_pos, col_pos = zeropos[zeroidx]
    # 가로 체크
    if number in board[row_pos]:
        return False

    # 세로 체크
    for i in range(9):
        if board[i][col_pos] == number:
            return False

    # 네모 체크
    row_start, col_start = (row_pos//3)*3, (col_pos//3)*3
    for i in range(row_start, row_start+3):
        for j in range(col_start, col_start+3):
            if board[i][j] == number:
                return False

    return True

def bt(idx):
    if idx == len(zeropos):
        for j in range(9):
            print(' '.join(map(str, board[j])))
        exit()

    for i in range(1, 10):
        if check(idx, i, board):
            row_pos, col_pos = zeropos[idx]
            board[row_pos][col_pos] = i
            bt(idx+1)
            board[row_pos][col_pos] = 0


sdocu = []
zeropos = []

for i in range(9):
    data = list(map(int, input().split()))
    for j in range(9):
        if data[j] == 0:
            zeropos.append((i, j))
    sdocu.append(data)

board = [a[:] for a in sdocu]
bt(0)