def smallest_fishbool():
    global board
    MIN = min(board)
    for idx, b in enumerate(board):
        if b == MIN:
            board[idx] = b+1

def high_fishbool():
    global board
    new_board = []
    a = [board[0]]
    b = board[1:]
    new_board.append(a)
    new_board.append(b)
    board = [n[:] for n in new_board]

    while True:
        height = len(board)
        width = len(board[-1]) - len(board[0])

        if width - height < 0:
            return

        mv_row, mv_col = height, len(board[0])

        # 바꿔야 하는 것 떼어 오기
        tmp = []
        for r in range(mv_row):
            tmp_r = []
            for c in range(mv_col):
                tmp_r.append(board[r][c])
            tmp.append(tmp_r)

        # 떼어 온 것 회전
        rotate = list(map(list, zip(*tmp[::-1])))

        new_board = []
        for i in range(len(rotate)):
            new_board.append(rotate[i])
        new_board.append(board[-1][mv_col:])
        # new_board.append(board[-1])
        board = [n[:] for n in new_board]

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
    height, width = len(board), len(board[-1]) # 이것때매 틀림 0으로 해서
    for i in range(height):
        for j in range(width):
            for k in range(2):
                drow, dcol = i + dx[k], j + dy[k]
                if not checkout(i, j) and not checkout(drow, dcol): # 범위안에 들면
                    diff = abs(board[i][j]-board[drow][dcol])//5
                    # print(i, j, drow, dcol)
                    # print(diff)
                    if diff:
                        if board[i][j] > board[drow][dcol]: # 원래가 더크면
                            tmp_board[i][j] -= diff
                            tmp_board[drow][dcol] += diff
                        elif board[i][j] < board[drow][dcol]:
                            tmp_board[i][j] += diff
                            tmp_board[drow][dcol] -= diff
                    # print(tmp_board)
    board = [a[:] for a in tmp_board]

def oneline_fishbool(): # 재검
    global board
    tmp = []
    height, width = len(board), len(board[-1])
    for i in range(width):
        for j in range(height-1, -1, -1):
            if not checkout(j, i):
                tmp.append(board[j][i])
    board = tmp[:]


def fly_fishbool():
    global board
    tmp_board = []
    N = len(board)
    # 한번 자르기
    cut_front = board[:N//2]
    cut_front.reverse()
    cut_back = board[N//2:]
    tmp_board.append(cut_front)
    tmp_board.append(cut_back)
    board = [a[:] for a in tmp_board]

    # 두번 자르기
    tmp_board, left_board = [], []
    for i in range(2):
        t, l = [], []
        for j in range(N // 2):
            if j < N // 4:
                t.append(board[i][j])
            else:
                l.append(board[i][j])
        tmp_board.append(t)
        left_board.append(l)
    # print(tmp_board)
    # print(left_board)

    # 돌리기
    rotate1 = list(map(list, zip(*tmp_board[::-1])))
    rotate2 = list(map(list, zip(*rotate1[::-1])))

    # 붙이기
    new_board = []
    for i in range(len(rotate2)):
        new_board.append(rotate2[i])
    for i in range(len(left_board)):
        new_board.append(left_board[i])

    board = [a[:] for a in new_board]

def simulate():
    if max(board) - min(board) <= K:
        return 0
    else:
        cnt = 1

    while True:
        # print("cnt", cnt)
        # 물고기 가장 작은 어항 +1
        smallest_fishbool()
        # print("물고기 가장 작은 어항 +1")
        # print(board)

        # 어항 쌓기
        high_fishbool()

        # print("어항 쌓기")
        # print(board)

        # 물고기 수 조절
        adjust_fishbool()

        # print("물고기 수 조절")
        # print(board)

        # 일렬로 놓기
        oneline_fishbool()

        # print("일렬로 놓기")
        # print(board)

        # 공중부양 작업
        fly_fishbool()
        # print("공중부양 작업")
        # print(board)

        # 물고기 수 조절
        adjust_fishbool()
        # print("물고기 수 조절")
        # print(board)

        # 일렬로 놓기
        oneline_fishbool()
        # print("일렬로 놓기")
        # print(board)

        if max(board) - min(board) <= K:
            # print(board)
            return cnt
        else:
            cnt += 1

N, K = map(int, input().split())
board = list(map(int, input().split()))
print(simulate())