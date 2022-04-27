from copy import deepcopy
from collections import deque

def checkout(row, col):
    if row<0 or row>=size or col<0 or col>=size:
        return True
    return False

def turn_ice(row, col, blocksize):
    tmp = [[0]*blocksize for _ in range(blocksize)]
    after = [[0]*blocksize for _ in range(blocksize)]

    for i in range(row, row+blocksize):
        for j in range(col, col+blocksize):
            tmp[i-row][j-col] = board[i][j]

    for i in range(blocksize):
        for j in range(blocksize):
            after[j][blocksize-1-i] = tmp[i][j]
    return after

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def simulate():
    global board
    for l in L:
        block = 2 ** l
        newboard = [[0]*size for _ in range(size)]

        for i in range(0, size, block):
            for j in range(0, size, block):
                tmp = turn_ice(i, j, block)

                for row in range(block):
                    for col in range(block):
                        newboard[i+row][j+col] = tmp[row][col]

        # print(newboard)
        minusboard = [[0] * size for _ in range(size)]

        for i in range(size):
            for j in range(size):

                cnt = 0
                if newboard[i][j] == 0:
                    continue

                for d in range(4):
                    drow, dcol = i+dx[d], j+dy[d]
                    if checkout(drow, dcol) or newboard[drow][dcol] == 0: # 범위에 있고 얼음 있으면
                        continue
                    cnt += 1

                if cnt<3:
                    minusboard[i][j] = newboard[i][j]-1
                else:
                    minusboard[i][j] = newboard[i][j]

        board = deepcopy(minusboard)

def check_bfs(row, col):
    visit = [[False]*size for _ in range(size)]
    queue = deque()
    queue.append((row, col))
    visit[row][col] = True
    cnt = 0

    while queue:
        now_x, now_y = queue.popleft()
        cnt += 1
        for i in range(4):
            drow, dcol = now_x+dx[i], now_y+dy[i]
            if not checkout(drow, dcol) and visit[drow][dcol] == False and board[drow][dcol]>0:
                visit[drow][dcol] = True
                queue.append((drow, dcol))
    return cnt


N, Q = map(int, input().split())
size = 2**N
board = []

for _ in range(size):
    board.append(list(map(int, input().split())))
L = list(map(int, input().split()))
simulate()
# print(board)

answer_sum = 0
answer_size = 0


for i in range(size):
    for j in range(size):
        answer_sum += board[i][j]
        if board[i][j] > 0:
            count = check_bfs(i, j)
            if count>1:
                answer_size = max(answer_size, count)

print(answer_sum)
print(answer_size)