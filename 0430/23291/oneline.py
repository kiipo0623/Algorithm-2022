def checkout(row, col):
    global board
    if row < 0 or row >= len(board):
        return True
    elif col < 0 or col >= len(board[row]):
        return True
    return False

def oneline_fishbool():
    global board
    tmp = []
    height, width = len(board), len(board[-1])
    for i in range(width):
        for j in range(height-1, -1, -1):
            if not checkout(j, i):
                tmp.append(board[j][i])
    board = tmp[:]

board = [[5, 3], [10, 6], [9, 5, 10, 8]]
oneline_fishbool()
print(board)
