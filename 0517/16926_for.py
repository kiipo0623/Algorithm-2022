N, M, R = map(int, input().split())

# N : 가로 길이 M : 세로 길이
def rotate(idx, cnt):
    for _ in range(cnt):
        save = board[idx][idx]
        # 위쪽
        for c in range(idx, M-idx-1):
            board[idx][c] = board[idx][c+1]
        # 오른쪽
        for r in range(idx, N-idx-1):
            board[r][M-idx-1] = board[r+1][M-idx-1]

        # 아래쪽
        for c in range(M-idx-1, idx, -1):
            board[N-idx-1][c] = board[N-idx-1][c-1]

        # 왼쪽
        for r in range(N-idx-1, idx, -1):
            board[r][idx] = board[r-1][idx]

        board[idx+1][idx] = save

board = []
for _ in range(N):
    board.append(list(map(int, input().split())))

for idx in range(min(N, M)//2):
    rotate(idx, R)

for i in range(N):
    print(' '.join(map(str, board[i])))

