def checkout(row, col):
    global board
    if row < 0 or row >= len(board):
        return True
    elif col < 0 or col >= len(board[row]):
        return True
    return False


board = [[3, 3], [14, 5], [9, 3, 11, 8]]
print(checkout(2, 3))
