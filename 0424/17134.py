from copy import deepcopy
dx = [-1, 1, 0, 0]
dy = [0, 0, 1, -1]
directmove = {0:1, 1:0, 2:3, 3:2}

def move_shark(b):
    after = [[False] * C for _ in range(R)]
    for sharknum in range(1, M+1):
        # 상어 죽었으면
        if sharkdict[sharknum] == False:
            continue

        row, col, speed, direct, size = sharkdict[sharknum]
        # 횟수만큼 이동
        for cnt in range(speed):
            drow, dcol = row + dx[direct], col + dy[direct]
            if drow < 0 or drow >= R or dcol < 0 or dcol >= C:
                direct = directmove[direct]
                drow, dcol = row + dx[direct], col + dy[direct]
            row, col = drow, dcol

        if after[row][col]:
            after[row][col].append(sharknum)
        else:
            after[row][col] = [sharknum]
        sharkdict[sharknum] = [row, col, speed, direct, size]
    return after

def eat_shark(b):
    for row in range(R):
        for col in range(C):
            if b[row][col] and len(b[row][col]) >= 2:
                # 제일 큰 놈 찾기
                maxsize, maxshark = -1, -1
                for sharknum in b[row][col]:
                    _, _, _, _, size = sharkdict[sharknum]
                    if size>maxsize:
                        maxsize, maxshark = size, sharknum
                # 나머지 놈 죽이기
                for sharknum in b[row][col]:
                    if sharknum != maxshark:
                        sharkdict[sharknum] = False
                # 보드 갱신하기
                b[row][col] = [maxshark]
    return b

def simulate():
    global answer, board
    for c in range(0, C+1):
        if c == C:
            return

        if c >= 0:
            for r in range(R):
                if board[r][c] != 0:
                    # 보드에서상어 없애기 점수 더하기 딕셔너리 정리
                    sharknum = board[r][c][0]
                    answer += sharkdict[sharknum][4]
                    board[r][c] = 0
                    sharkdict[sharknum] = False
                    break

        # 상어 이동
        aftermove = move_shark(board)

        # 상어 먹기
        aftereat = eat_shark(aftermove)
        board = deepcopy(aftereat)


R, C, M = map(int, input().split())
sharkdict = dict()
answer = 0
board = [[False]*C for _ in range(R)]
for i in range(1, M+1):
    r, c, s, d, z = map(int, input().split())
    r, c, d = r-1, c-1, d-1
    sharkdict[i] = [r, c, s, d, z]
    board[r][c] = [i]

simulate()
print(answer)