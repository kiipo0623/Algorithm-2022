from collections import deque

# 상 우 하 좌
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

def checkout(r, c):
    return r<0 or c<0 or r>=N or c>=N

def simulation():
    global mvtime
    time = 0
    snake = deque()
    snake.append((0, 0))
    nowdir = 1


    while True:
        time += 1

        if mvtime and time-1 == mvtime[0]:
            mvtime.popleft()
            D = mvdir.popleft()
            if D == 'L':
                nowdir = (nowdir-1)%4
            elif D == 'D':
                nowdir = (nowdir+1)%4


        # 대가리 이동
        head_row, head_col = snake[0]
        drow, dcol = head_row+dx[nowdir], head_col+dy[nowdir]

        if checkout(drow, dcol) or (drow, dcol) in snake:
            return time
        # 무조건 집어넣는데 ..
        snake.appendleft((drow, dcol))

        # 사과 있는지
        if board[drow][dcol]:
            board[drow][dcol] = 0
            continue
        else:
            snake.pop()


N = int(input())
K = int(input())
board = [[0 for _ in range(N)] for _ in range(N)]
mvdir = deque()
mvtime = deque()

for _ in range(K):
    R, C = map(int, input().split())
    R, C = R-1, C-1
    board[R][C] = 1

L = int(input())

for _ in range(L):
    X, C = input().split()
    X = int(X)
    mvdir.append(C)
    mvtime.append(X)


print(simulation())

