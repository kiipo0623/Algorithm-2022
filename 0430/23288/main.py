from collections import deque
# 동 남 서 북
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

dice = {'back':2, 'up':1, 'front':5, 'down':6, 'left':4, 'right':3}

def can_move(row, col, dir):
    if dir == 0 and col >= M-1:
        return 2
    if dir == 1 and row >= N-1:
        return 3
    if dir == 2 and col <= 0:
        return 0
    if dir == 3 and row <= 0:
        return 1
    else:
        return dir

def move_dice(dir):
    # 동쪽
    if dir == 0:
        dice['down'], dice['right'], dice['up'], dice['left'] = dice['right'], dice['up'], dice['left'], dice['down']
    # 남쪽
    elif dir == 1:
        dice['down'], dice['front'], dice['up'], dice['back'] = dice['front'], dice['up'], dice['back'], dice['down']
    # 서쪽
    elif dir == 2:
        dice['down'], dice['left'], dice['up'], dice['right'] = dice['left'], dice['up'], dice['right'], dice['down']
    # 북쪽
    elif dir == 3:
        dice['back'], dice['up'], dice['front'], dice['down'] = dice['up'], dice['front'], dice['down'], dice['back']

def checkout(row, col):
    if row<0 or row>=N or col<0 or col>=M:
        return True
    return False

def bfs(row, col):
    queue = deque([])
    queue.append((row, col))
    visit = [[False]*M for _ in range(N)]
    cnt = 1
    value = board[row][col]
    visit[row][col] = True

    while queue:
        now_r, now_c = queue.popleft()
        for k in range(4):
            drow, dcol = now_r + dx[k], now_c + dy[k]
            if not checkout(drow, dcol) and not visit[drow][dcol] and board[drow][dcol]==value:
                queue.append((drow, dcol))
                visit[drow][dcol] = True
                cnt += 1

    return cnt

def simulate():
    global answer
    row, col, dir = 0, 0, 0
    for _ in range(K):
        # 이동 방향으로 굴러감
        dir = can_move(row, col, dir)
        # print("dir ", dir)
        # 좌표 이동
        row, col = row + dx[dir], col + dy[dir]
        # 주사위 이동
        move_dice(dir)

        # 점수 획득
        B = board[row][col]
        C = bfs(row, col)
        answer += B*C

        # 이동 방향 결정
        A = dice['down']
        if A > B:
            dir = (dir+1)%4
        elif A < B:
            dir = (dir-1)%4

        # print(dice)


N, M, K = map(int, input().split())
answer = 0
board = []
for _ in range(N):
    board.append(list(map(int, input().split())))
simulate()
print(answer)