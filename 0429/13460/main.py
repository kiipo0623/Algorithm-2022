dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
def find(s):
    for i in range(N):
        for j in range(N):
            if board[i][j] == s:
                return i, j

def bt(b, cnt):
    if cnt>=answer:
        return

    save = [a[:] for a in b]
    r_row, r_col = find('R')
    b_row, b_col = find('B')

    mv_red, mv_blue = True, True
    hole_red, hole_blue = False, False

    # 상
    while True:
        if mv_red == True:
            r_drow, r_dcol = r_row + dx[0], r_col + dy[0]
            if board[r_dcol][r_dcol] == '#':
                mv_red = False
            elif board[r_dcol][r_drow] == 'O': # 끝
                hole_red = True
                mv_red = False
            # else:
            #     board[r_row][r_col] = '.'
            #     board[r_drow][r_dcol] = 'R'
            #     r_row, r_col = r_drow, r_dcol

        if mv_blue == True:
            b_drow, b_dcol = b_row + dx[0], b_col + dy[0]
            if board[b_dcol][b_dcol] == '#':
                mv_blue = False
            elif board[r_dcol][r_drow] == 'O':  # 끝
                hole_red = True






N, M = map(int, input().split())
board = []
red_row, red_col, blue_row, blue_col, hole_row, hole_col =0, 0, 0, 0, 0, 0
answer = 11
for i in range(N):
    data = list(input())
    for j in range(M):
        if data[j] == 'O':
            hole_row, hole_col = i, j
        elif data[j] == 'R':
            red_row, red_col = i, j
        elif data[j] == 'B':
            blue_row, blue_col = i, j
    board.append(data)

