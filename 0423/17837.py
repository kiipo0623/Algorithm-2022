# 방향을 두 곳에서 관리하는 이유가 잇니 ..
from collections import deque
# 체스판 : deque([말번호])
# horse
# 말번호 : [말row좌표, 말col좌표, 방향]

dx = [0, 0, 0, -1, 1]
dy = [0, 1, -1, 0, 0]
direction = {1:2, 2:1, 3:4, 4:3}
# 호 방향
def white(h_idx, row, col, drow, dcol, ddir):
    global chess
    temp = [] # 반대로 담김

    while True:
        now = chess[row][col].pop()
        temp.append(now)
        horse[now[0]] = [drow, dcol, now[1]]

        if now == h_idx:
            break
    horse[h_idx] = [drow, dcol, ddir]

    if chess[drow][dcol]:
        chess[drow][dcol].extend(list(reversed(temp)))
    else:
        chess[drow][dcol] = deque(reversed(temp))

    if len(chess[row][col]) == 0:
        chess[row][col] = False

def red(h_idx, row, col, drow, dcol, ddir):
    global chess
    temp = [] # 반대로 담김

    while True:
        now = chess[row][col].pop()
        temp.append(now)
        horse[now[0]] = [drow, dcol, now[1]]
        if now == h_idx:
            break
    horse[h_idx] = [drow, dcol, ddir]
    if chess[drow][dcol]:
        chess[drow][dcol].extend(temp)
    else:
        chess[drow][dcol] = deque(temp)

    if len(chess[row][col]) == 0:
        chess[row][col] = False

def simulate():
    for i in range(1, 1001): # 시간
        for h_idx in range(1, K+1): # 말 한개씩 순서대로
            row, col, dir = horse[h_idx]
            drow, dcol = row + dx[dir], col + dy[dir]

            if board[drow][dcol] == 0: # 흰색
                white(h_idx, row, col, drow, dcol, dir)

            elif board[drow][dcol] == 1: # 빨간색
                red(h_idx, row, col, drow, dcol, dir)

            elif board[drow][dcol] == 2: # 파란
                new_dir = direction[dir]
                nrow, ncol = row + dx[new_dir], col + dy[new_dir]
                print("new_dir", new_dir)

                horse[h_idx] = [row, col, new_dir]
                if board[nrow][ncol] == 1:
                    red(h_idx, row, col, nrow, ncol, new_dir)
                elif board[nrow][ncol] == 0:
                    white(h_idx, row, col, nrow, ncol, new_dir)

            print("h_idx", h_idx, "color", board[drow][dcol])
            print("chess")
            print(chess)
            print("horse")
            print(horse)
            x, y = horse[h_idx][0], horse[h_idx][1]
            if chess[x][y] and len(chess[x][y]) >= 4:
                return i

    return -1
N, K = map(int, input().split())

board = []
chess = [[False]*(N+2) for _ in range(N+2)]

board.append([2]*(N+2))
for _ in range(N):
    board.append([2] + list(map(int, input().split())) + [2])
board.append([2]*(N+2))

horse = dict()
for i in range(1, K+1):
    x, y, d = map(int, input().split())
    q = deque()
    q.append([i, d])
    chess[x][y] = q
    horse[i] = [x, y, d]

print(board)

print(simulate())



