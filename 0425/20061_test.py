def putblock(t, x, y):
    if t == 1:
        for i in range(-1, 6):  # 파란색
            if blue_board[x][i + 1] == True:
                blue_board[x][i] = True
                break

        for i in range(-1, 6):  # 초록색
            if green_board[i + 1][y] == True:
                green_board[i][y] = True
                break

    elif t == 2:
        for i in range(1, 6):
            if blue_board[x][i + 1] == True:
                blue_board[x][i - 1] = True
                blue_board[x][i] = True
                break

        for i in range(0, 6):
            if green_board[i + 1][y] == True or green_board[i + 1][y + 1] == True:
                green_board[i][y] = True
                green_board[i][y + 1] = True
                break

    elif t == 3:
        for i in range(0, 6):
            if green_board[x][i + 1] == True or green_board[x + 1][i + 1] == True:
                green_board[x][i] = True
                green_board[x + 1][i] = True
                break

        for i in range(1, 6):
            if green_board[i + 1][y] == True:
                green_board[i - 1][y] = True
                green_board[i][y] = True
                break

red_board = [[False]*4 for _ in range(4)]
blue_board = [[False]*7 for _ in range(4)]
green_board = [[False]*4 for _ in range(7)]
for i in range(4):
    blue_board[i][6] = True
    green_board[6][i] = True

putblock(1, 1, 1)
putblock(2, 3, 0)

print("red")
print(red_board)
print("blue")
print(blue_board)
print("green")
print(green_board)