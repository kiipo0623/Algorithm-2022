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

def grade():
    global answer
    MIN = int(1e9)
    for i in range(N):
        MIN = min(MIN, sum(board[i]))
    answer = min(answer, MIN)

def simulate(todo):
    global board
    save = [a[:] for a in board]
    for do in todo:
        r, c, s = work[do]
        for i in range(1, s+1):
            circle(r, c, i)
    # print(board)
    grade()
    board = [a[:] for a in save]

def permutation(cnt, select, visit):
    if cnt == K:
        # print(select)
        simulate(select)

    for i in range(K):
        if visit[i] == False:
            select.append(lst[i])
            visit[i] = True
            permutation(cnt + 1, select, visit)
            select.pop()
            visit[i] = False


N, M, K = map(int, input().split())
board = []
work = []
lst = [i for i in range(K)]
answer = int(1e9)
for _ in range(N):
    board.append(list(map(int, input().split())))
for _ in range(K):
    r, c, s = map(int, input().split())
    r, c = r-1, c-1
    work.append((r, c, s))
permutation(0, [], [False]*K)
print(answer)
