from collections import deque
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]
def rotate(depth, R):
    queue = deque()
    row, col, k = depth, depth, 0
    # 뽑아오기
    while True:
        drow, dcol = row + dx[k], col + dy[k]
        if depth <= drow < N-depth and depth <= dcol < M-depth:
            queue.append(board[row][col])
            row, col = drow, dcol
        else:
            k += 1
        if row == depth and col == depth:
            break

    # 돌리기
    for _ in range(R):
        queue.rotate(-1)

    # 박기
    row, col, k = depth, depth, 0
    while queue:
        drow, dcol = row + dx[k], col + dy[k]
        if depth <= drow < N-depth and depth <= dcol < M-depth:
            board[row][col] = queue.popleft()
            row, col = drow, dcol
        else:
            k += 1


N, M, R = map(int, input().split())
board = []
for _ in range(N):
    board.append(list(map(int, input().split())))

for idx in range(min(N, M)//2):
    rotate(idx, R)


for i in range(N):
    print(' '.join(map(str, board[i])))
