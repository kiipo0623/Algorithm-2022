from collections import deque
direction = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
def checkout(row, col):
    if row<0 or row>=N or col<0 or col>=N:
        return True
    return False

def spring():
    global board, queue
    deadqueue = deque([])
    babyqueue = deque([])
    for i in range(N):
        for j in range(N):
            leng = len(board[i][j])
            for _ in range(leng):
                now = board[i][j].popleft()
                # 양분 먹음 나이증가 죽은나무 번식나무
                if food[i][j] >= now: # 가능
                    food[i][j] -= now # 양분 먹음
                    now += 1 # 나이 증가
                    board[i][j].append(now)

                    if now%5 == 0:
                        babyqueue.append((i, j))

                else: # 불가능
                    deadqueue.append((i, j, now))
    return deadqueue, babyqueue

def summer(deadqueue):
    global food
    for x, y, z in deadqueue:
        food[x][y] += (z//2)

def fall(babyqueue):
    global board
    for x, y in babyqueue:
        for i in range(8):
            drow, dcol = x+direction[i][0], y+direction[i][1]
            if checkout(drow, dcol):
                continue
            board[drow][dcol].appendleft(1)

def winter():
    global food
    for i in range(N):
        for j in range(N):
            food[i][j] += A[i][j]

def simulate():
    for i in range(K):
        deadq, babyq = spring()
        summer(deadq)
        fall(babyq)
        winter()

def count_tree():
    cnt = 0
    for i in range(N):
        for j in range(N):
            cnt += len(board[i][j])
    return cnt

N, M, K = map(int, input().split())
A = []
board = [[deque([]) for _ in range(N)] for _ in range(N)]
food = [[5]*N for _ in range(N)]
for _ in range(N):
    A.append(list(map(int, input().split())))
for _ in range(M):
    x, y, z = map(int, input().split())
    x, y = x-1, y-1
    board[x][y].append(z)
simulate()
print(count_tree())