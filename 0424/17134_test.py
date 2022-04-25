dx = [-1, 1, 0, 0]
dy = [0, 0, 1, -1]
directmove = {0: 1, 1: 0, 2: 3, 3: 2}


def move_shark(b):
    after = [[False] * C for _ in range(R)]
    for sharknum in range(1, M+1):
        # 상어 죽었으면
        if sharkdict[sharknum] == False:
            continue

        row, col, speed, direct, size = sharkdict[sharknum]
        # 횟수만큼 이동
        print("sharknum", sharknum, "speed", speed)
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


R, C, M = map(int, input().split())
sharkdict = dict()
answer = 0
board = [[False]*C for _ in range(R)]
for i in range(1, M+1):
    r, c, s, d, z = map(int, input().split())
    r, c, d = r-1, c-1, d-1
    sharkdict[i] = [r, c, s, d, z]
    board[r][c] = [i]

print(move_shark(board))

