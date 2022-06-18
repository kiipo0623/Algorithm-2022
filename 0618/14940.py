from collections import deque
n, m = map(int, input().split())
answer = [[-1]*m for _ in range(n)]
board = []
pos = [0, 0]

for i in range(n):
    t = list(map(int, input().split()))
    for j in range(m):
        if t[j] == 2:
            pos = [i, j]
        elif t[j] == 0:
            answer[i][j] = 0
    board.append(t)

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

answer[pos[0]][pos[1]] = 0

def solution(pos):
    global answer
    q = deque()
    q.append((1, pos[0], pos[1]))

    while q:
        cost, r, c = q.popleft()

        for k in range(4):
            drow, dcol = r+dx[k], c+dy[k]
            # 거리가 다 똑같으니까 처음 방문하는게 무조건 들어가야 한다
            if 0<=drow<n and 0<=dcol<m and answer[drow][dcol] == -1 and board[drow][dcol] == 1:
                    answer[drow][dcol] = cost
                    q.append((cost+1, drow, dcol))

solution(pos)
for i in range(n):
    print(' '.join(map(str, answer[i])))
