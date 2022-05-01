from copy import deepcopy
def checkout(row, col):
    global board
    if row < 0 or row >= len(board):
        return True
    elif col < 0 or col >= len(board[row]):
        return True
    return False

def adjust_fishbool():
    global board
    dx = [1, 0]
    dy = [0, 1]
    tmp_board = [a[:] for a in board]
    height, width = len(board), len(board[0])
    for i in range(height):
        for j in range(width):
            for k in range(2):
                drow, dcol = i + dx[k], j + dy[k]
                if not checkout(i, j) and not checkout(drow, dcol): # 범위안에 들면
                    diff = abs(board[i][j]-board[drow][dcol])//5
                    print(i, j, drow, dcol)
                    print(diff)
                    if diff:
                        if board[i][j] > board[drow][dcol]: # 원래가 더크면
                            tmp_board[i][j] -= diff
                            tmp_board[drow][dcol] += diff
                        elif board[i][j] < board[drow][dcol]:
                            tmp_board[i][j] += diff
                            tmp_board[drow][dcol] -= diff
                    print(tmp_board)
    board = [a[:] for a in tmp_board]


board =[[3,3], [14,5], [9,3,11,8]]
adjust_fishbool()
print(board)