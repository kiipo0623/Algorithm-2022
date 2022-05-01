def checkout(row, col, R0, C0, R, C):
    if row<R0 or col<C0 or row>R or col>C:
        return True
    return False

def circle(r, c, s):
    global board
    s_row, e_row, s_col, e_col = r-s, r+s, c-s, c+s
    tmp = board[s_row][e_col]
    drow, dcol = s_row, e_col

    # 위
    while not checkout(drow, dcol-1, s_row, s_col, e_row, e_col):
        board[drow][dcol] = board[drow][dcol-1]
        drow, dcol = drow, dcol - 1
    # 왼쪽
    while not checkout(drow+1, dcol, s_row, s_col,e_row, e_col):
        board[drow][dcol] = board[drow+1][dcol]
        drow, dcol = drow+1, dcol
    # 아래
    while not checkout(drow, dcol+1, s_row, s_col,e_row, e_col):
        board[drow][dcol] = board[drow][dcol+1]
        drow, dcol = drow, dcol+1

        # 오른쪽
    while not checkout(drow-1, dcol, s_row, s_col, e_row, e_col):
        if drow-1 == s_row and dcol == e_col:
            break
        board[drow][dcol] = board[drow-1][dcol]
        drow, dcol = drow-1, dcol

    board[drow][dcol] = tmp

board = []
N = 5
M = 6
for _ in range(N):
    board.append(list(map(int, input().split())))
circle(2, 3, 2)
circle(2,3,1)
print(board)