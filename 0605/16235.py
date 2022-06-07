from collections import deque
import heapq

newpos = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]

def update(i, j):
    global board, dead, baby
    L, flag, tmp = len(board[i][j]), False, []
    for _ in range(L):
        heapq.heapify(board[i][j])
        tree = heapq.heappop(board[i][j])
        # print("pop tree", tree)
        if flag:
            dead.append((i, j, tree))
        elif tree > food[i][j]:
            flag = True
            dead.append((i, j, tree))
        else:
            food[i][j] -= tree
            tmp.append(tree+1)
            if (tree+1) % 5 == 0:
                baby.append((i, j, tree+1))
    # print()
    if tmp:
        treepos.append((i, j))
    board[i][j] = tmp
    return


def spring():
    global board
    L = len(treepos)
    for _ in range(L):
        x, y = treepos.popleft()
        update(x, y)

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
                board[dr][dc].append(1)
                if (dr, dc) not in treepos:
                    treepos.append((dr, dc))

def winter():
    global food, A, treepos
    for i in range(N):
        for j in range(N):
            food[i][j] += A[i][j]

N, M, K = map(int, input().split())
A = []
board = [[[] for _ in range(N)] for _ in range(N)]
treepos = deque()

for _ in range(N):
    A.append(list(map(int, input().split())))
for _ in range(M):
    x, y, z = map(int, input().split())
    # 여기서 1씩 뺴줌
    board[x-1][y-1].append(z)
    treepos.append((x-1, y-1))

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