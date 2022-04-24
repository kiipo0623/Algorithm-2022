#
dx = [0, 0, 0, -1, 1]
dy = [0, 1, -1, 0, 0]
dir_change ={1:2, 2:1, 3:4, 4:3}

def white(h_idx, row, col, drow, dcol): # 검증 완
    stack = []
    while True:
        # 하나씩 빼기, 스택에 넣기, 딕셔너리 위치 갱신
        now = chess[row][col].pop()
        stack.append(now)
        horse[now][0], horse[now][1] = drow, dcol

        if now == h_idx:
            break

    # 새로운 chess에 붙이기
    if chess[drow][dcol]:
        chess[drow][dcol].extend(list(reversed(stack)))
    else:
        chess[drow][dcol] = list(reversed(stack))

    # 원래 자리 False로
    if len(chess[row][col]) == 0:
        chess[row][col] = False

def red(h_idx, row, col, drow, dcol):
    stack = []
    while True:
        # 하나씩 빼기, 스택에 넣기, 딕셔너리 위치 갱신
        now = chess[row][col].pop()
        stack.append(now)
        horse[now][0], horse[now][1] = drow, dcol

        if now == h_idx:
            break

    # 새로운 chess에 붙이기
    if chess[drow][dcol]:
        chess[drow][dcol].extend(stack)
    else:
        chess[drow][dcol] = stack

    # 원래 자리 False로
    if len(chess[row][col]) == 0:
        chess[row][col] = False


def simulate():
    for time in range(1, 1001):
        for h_idx in range(1, K+1):
            # print(h_idx)
            h_val = horse[h_idx]
            row, col, dir = h_val
            drow, dcol = row+dx[dir], col+dy[dir]
            # print("now", h_idx, "before", row, col, "after", drow, dcol)

            if board[drow][dcol] == 0: # 흰색일때
                white(h_idx, row, col, drow, dcol)

            elif board[drow][dcol] == 1: # 빨간색일때
                red(h_idx, row, col, drow, dcol)

            elif board[drow][dcol] == 2: # 파란색일떄
                new_dir = dir_change[dir]
                horse[h_idx] = [row, col, new_dir]
                drow, dcol = row + dx[new_dir], col + dy[new_dir]
                if board[drow][dcol] == 0:
                    white(h_idx, row, col, drow, dcol)
                elif board[drow][dcol] == 1:
                    red(h_idx, row, col, drow, dcol)
                elif board[drow][dcol] == 2:
                    pass

            # print("board")
            # print(board)
            # print("chess")
            # print(chess)
            # print("horse")
            # print(horse)
            # 종료 조건일 때
            if chess[drow][dcol] and len(chess[drow][dcol])>=4:
                return time
    return -1

N, K = map(int, input().split())
board, chess, horse = [], [[False]*(N+2) for _ in range(N+2)], dict()
board.append([2]*(N+2))

for _ in range(N):
    board.append([2]+list(map(int, input().split()))+[2])
board.append([2]*(N+2))


for idx in range(1, K+1):
    x, y, d = map(int, input().split())
    chess[x][y] = [idx]
    horse[idx] = [x, y, d]
# print("beforehorse", horse)

print(simulate())