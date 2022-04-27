from collections import deque
from copy import deepcopy

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

def checkout(row, col):
    if row<0 or row>=N or col<0 or col>=N:
        return True
    return False

def find(visited, color):
    for i in range(N):
        for j in range(N):
            if visited[i][j] == True and board[i][j] == color:
                return i, j


def bfs(row, col, todo):
    visited = [[False]*N for _ in range(N)]
    queue = deque()
    queue.append((row, col))
    visited[row][col] = True
    size, rainbow = 1, 0

    while queue:
        nrow, ncol = queue.popleft()
        for i in range(4):
            drow, dcol = nrow+dx[i], ncol+dy[i]
            if not checkout(drow, dcol) and visited[drow][dcol] == False:
                if board[drow][dcol] == board[row][col] or board[drow][dcol] == -2:
                    visited[drow][dcol] = True
                    size += 1
                    queue.append((drow, dcol))
                    if board[drow][dcol] == -2:
                        rainbow += 1

    if todo == True: # 블록 추가 용도
        x, y = find(visited, board[row][col])
        if size>=2:
            blockgroup.add((size, rainbow, x, y))
        return
    else: #보드 갱신 용
        return visited

def find_blockgroup():
    for i in range(N):
        for j in range(N):
            if board[i][j] > 0:
                bfs(i, j, True)

def ground(board):
    newboard = [[0]*N for _ in range(N)]
    for i in range(N):
        col = list(map(list, zip(*board)))[i]
        cnt = 0

        for idx in range(N - 1, -1, -1):
            if col[idx] == 0:
                cnt += 1
            elif col[idx] == -1:
                cnt = 0
            else:
                if cnt>0:
                    col[idx + cnt] = col[idx]
                    col[idx] = 0

        for j in range(N):
            newboard[j][i] = col[j]
    return newboard


def simulate():
    global board, blockgroup, answer
    while True: # 블록그룹 초기화 해주기 매턴마다
        blockgroup = set()
        find_blockgroup()
        blockgroup = list(blockgroup)

        if len(blockgroup) == 0:
            break

        blockgroup.sort(key=lambda x: (-x[0], -x[1], -x[2], -x[3]))
        size, rainbow, r, c = blockgroup[0]
        v = bfs(r, c, False)

        for i in range(N):
            for j in range(N):
                if v[i][j] == True:
                    board[i][j] = 0

        answer += size*size
        nb = ground(board)
        cb = list(map(list, zip(*nb)))[::-1]
        ab = ground(cb)
        board = deepcopy(ab)


N, M = map(int, input().split())

board = []
blockgroup = set()
answer = 0

for _ in range(N):
    data = list(map(int, input().split()))
    for j in range(N):
        if data[j] == 0:
            data[j] = -2
    board.append(data)

simulate()


print(answer)