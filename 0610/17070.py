def backtrack(dir, row, col):
    global answer, board
    if row == N and col == N:
        answer += 1
        return

    # 가로 방향
    if dir == 0:
        if 0 <= col + 1 <= N and board[row][col + 1] == 0:
            backtrack(0, row, col + 1)

        cnt = 0
        for d in [(1, 0), (1, 1), (0, 1)]:
            drow, dcol = row + d[0], col + d[1]
            if 0 <= drow <= N and 0 <= dcol <= N and board[drow][dcol] == 0:
                cnt += 1

        if cnt == 3:
            backtrack(2, row + 1, col + 1)

    # 세로 방향
    elif dir == 1:
        if 0 <= row + 1 <= N and board[row + 1][col] == 0:
            backtrack(1, row + 1, col)

        cnt = 0
        for d in [(1, 0), (1, 1), (0, 1)]:
            drow, dcol = row + d[0], col + d[1]
            if 0 <= drow <= N and 0 <= dcol <= N and board[drow][dcol] == 0:
                cnt += 1

        if cnt == 3:
            backtrack(2, row + 1, col + 1)

    # 대각선 방향
    elif dir == 2:
        if 0 <= col + 1 <= N and board[row][col + 1] == 0:
            backtrack(0, row, col + 1)

        if 0 <= row + 1 <= N and board[row + 1][col] == 0:
            backtrack(1, row + 1, col)

        cnt = 0
        for d in [(1, 0), (1, 1), (0, 1)]:
            drow, dcol = row + d[0], col + d[1]
            if 0 <= drow <= N and 0 <= dcol <= N and board[drow][dcol] == 0:
                cnt += 1

        if cnt == 3:
            backtrack(2, row + 1, col + 1)

N = int(input())
board = [[1]*(N+2)]
for _ in range(N):
    board.append([1] + list(map(int, input().split())) + [1])
board.append([1]*(N+2))


board[1][1] = 1
board[1][2] = 1
answer = 0

# 0 가로 1 세로 2 대각선
backtrack(0, 1, 2)
print(answer)