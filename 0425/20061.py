def putblock(t, x, y):
    global grade, blue_board, red_board, green_board
    if t == 1:
        for i in range(0, 6):  # 파란색
            if blue_board[x][i + 1] == True:
                blue_board[x][i] = True
                break

        for i in range(0, 6):  # 초록색
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
            if blue_board[x][i + 1] == True or blue_board[x + 1][i + 1] == True:
                blue_board[x][i] = True
                blue_board[x + 1][i] = True
                break

        for i in range(1, 6):
            if green_board[i + 1][y] == True:
                green_board[i - 1][y] = True
                green_board[i][y] = True
                break

def getgrade():
    global grade, blue_board, red_board, green_board
    blue_remove, green_remove = [], []
    for col in range(5, 1, -1):
        blue_cnt, green_cnt = 0, 0
        for row in range(0, 4):
            if blue_board[row][col] == True:
                blue_cnt += 1
            if green_board[col][row] == True:
                green_cnt += 1
        if blue_cnt == 4:
            blue_remove.append(col)
            grade += 1
        if green_cnt == 4:
            grade += 1
            green_remove.append(col)

    for col in blue_remove:
        # blue_board[0][col], blue_board[1][col], blue_remove[2][col], blue_remove[3][col] = False, False, False, False
        for update in range(col-1, -1, -1):
            for i in range(4):
                blue_board[i][update+1] = blue_board[i][update]
        for i in range(4):
            blue_board[i][0] = False

    # print("rmv", green_remove)
    for row in green_remove:
        # green_board[row][0], green_board[row][1], green_remove[row][2], green_remove[row][3] = False, False, False, False
        for update in range(row-1, -1, -1):
            for i in range(4):
                green_board[update+1][i] = green_board[update][i]
        for i in range(4):
            green_board[0][i] = False

def specialdo():
    global grade, blue_board, red_board, green_board
    blue_checker, green_checker = [False, False], [False, False]
    for col in range(2):
        for row in range(4):
            if blue_board[row][col] == True:
                blue_checker[col] = True
            if green_board[col][row] == True:
                green_checker[col] = True

    if blue_checker.count(True):
        k = 1
        if blue_checker.count(True) == 2:
            k = 2
        start = 5-blue_checker.count(True)
        for i in range(start, -1, -1):
            for j in range(4):
                blue_board[j][i+k] = blue_board[j][i]

        for a in range(k):
            for i in range(4):
                blue_board[i][a]= False

    if green_checker.count(True):
        k = 1
        if green_checker.count(True) == 2:
            k = 2
        start = 5-green_checker.count(True)
        for i in range(start, -1, -1):
            for j in range(4):
                green_board[i+k][j] = green_board[i][j]
        for a in range(k):
            for i in range(4):
                green_board[a][i]= False


def simulate():
    for t, x, y in work:
        # print("start:", t,x,y)
        putblock(t, x, y)
        # print("----after put-----")
        # print(green_board)
        getgrade()
        # print("----after get----")
        # print(green_board)
        specialdo()
        # print("----after spe----")
        # print(green_board)

        # print("blue")
        # print(blue_board)
        # print("green")
        # print(green_board)


red_board = [[False]*4 for _ in range(4)]
blue_board = [[False]*7 for _ in range(4)]
green_board = [[False]*4 for _ in range(7)]
for i in range(4):
    blue_board[i][6] = True
    green_board[6][i] = True

grade = 0

N = int(input())
work = []
for _ in range(N):
    work.append(list(map(int, input().split())))

simulate()

answer = -4
for i in range(4):
    answer += blue_board[i].count(True)
for i in range(6):
    answer += green_board[i].count(True)

print(grade)
print(answer)