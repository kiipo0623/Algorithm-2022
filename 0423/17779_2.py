def make_d1d2(row, col):
    both = []
    d1, d2 = [], []
    for i in range(1, N-row+1):
        both.append(i)
    for i in range(1, col):
        d1.append(i)
    for i in range(1, N-col+1):
        d2.append(i)
    return [both, d1, d2]

def make_xy():
    xy_cand = []
    for i in range(1, N-1):
        for j in range(1, N-1):
            xy_cand.append((i, j))
    return xy_cand

def checkpeople(board):
    global graph
    one, two, three, four, five = 0, 0, 0, 0, 0
    for i in range(1, N+1):
        for j in range(1, N+1):
            if board[i][j] == 1:
                one += graph[i-1][j-1]
            elif board[i][j] == 2:
                two += graph[i-1][j-1]
            elif board[i][j] == 3:
                three += graph[i-1][j-1]
            elif board[i][j] == 4:
                four += graph[i-1][j-1]
            elif board[i][j] == 5:
                five += graph[i-1][j-1]
    min_, max_ = min(one, two, three, four, five), max(one, two, three, four, five)
    ans = max_-min_
    return ans

def garrimandering(row, col, d1, d2):
    UP, DOWN, LEFT, RIGHT = (row, col), (row+d1+d2, col-d1+d2), (row+d1, col-d1), (row+d2, col+d2)
    board = [[0]*(N+1) for _ in range(N+1)]

    for i in range(d1+1):
        board[row+i][col-i] = 5
        board[row + d2 + i][col + d2 - i] = 5
    for i in range(d2+1):
        board[row+i][col+i] = 5
        board[row + d1 + i][col - d1 + i] = 5

    # 5번 선거구
    for i in range(UP[0]+1, DOWN[0]):
        flag = False
        for j in range(N+1):
            if flag == True:
                board[i][j] = 5
            if flag and board[i][j] == 5:
                break
            if not flag and board[i][j] == 5:
                flag = True

    # 1번 선거구
    for i in range(1, LEFT[0]):
        for j in range(1, UP[1]+1):
            if board[i][j] == 0:
                board[i][j] = 1

    # 2번 선거구
    for i in range(1, RIGHT[0]+1):
        for j in range(UP[1]+1, N+1):
            if board[i][j] == 0:
                board[i][j] = 2

    # 3번 선거구
    for i in range(LEFT[0], N+1):
        for j in range(1, DOWN[1]):
            if board[i][j] == 0:
                board[i][j] = 3

    # 4번 선거구
    for i in range(RIGHT[0]+1, N+1):
        for j in range(DOWN[1], N+1):
            if board[i][j] == 0:
                board[i][j] = 4

    return checkpeople(board)


N = int(input())
graph = []
for _ in range(N):
    graph.append(list(map(int, input().split())))

xy_candidate = make_xy()
MIN = int(1e9)

for row, col in xy_candidate:
    both, d1, d2 = make_d1d2(row, col)
    for one in d1:
        for two in d2:
            if one+two in both:
                sol = garrimandering(row, col, one, two)
                MIN = min(MIN, sol)

print(MIN)