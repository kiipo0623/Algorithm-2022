from collections import deque
import sys
input = sys.stdin.readline

newpos = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]

def update(i, j):
    global board, dead, baby
    queue = board[i][j]
    tmp = deque()
    while queue:
        tree = queue.popleft()

        if tree > food[i][j]:
            dead.append((i, j, tree))
        else:
            food[i][j] -= tree
            tmp.append(tree+1)
            if (tree+1) % 5 == 0:
                baby.append((i, j, tree+1))
    board[i][j] = tmp

def spring():
    global board
    for i in range(N):
        for j in range(N):
            if board[i][j]:
                update(i, j)

def summer():
    global dead, food
    while dead:
        row, col, age = dead.popleft()
        food[row][col] += age//2

def fall():
    global baby, board
    while baby:
        row, col, age = baby.popleft()
        for dx, dy in newpos:
            dr, dc = row+dx, col+dy
            if 0<=dr<N and 0<=dc<N:
                board[dr][dc].appendleft(1)

def winter():
    global food, A
    for i in range(N):
        for j in range(N):
            food[i][j] += A[i][j]

N, M, K = map(int, input().split())
A = []
board = [[deque() for _ in range(N)] for _ in range(N)]

for _ in range(N):
    A.append(list(map(int, input().split())))
for _ in range(M):
    x, y, z = map(int, input().split())
    # 여기서 1씩 뺴줌
    board[x-1][y-1].append(z)

food = [[5]*N for _ in range(N)]

dead = deque()
baby = deque()

for i in range(K):
    # print("초기")
    # print(board)
    # print(food)
    # print()
    spring()
    # print("---spring---")
    # print(board)
    summer()
    # print("---summer---")
    # print(food)
    fall()
    # print("---fall---")
    # print(board)
    winter()
    # print("---winter---")
    # print(food)

answer = 0
for i in range(N):
    for j in range(N):
        answer += len(board[i][j])
print(answer)