from collections import deque
# RIGHT DOWN LEFT UP
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

# 0up 1top 2dowm 3bottom 4left 5right
dice = [2, 1, 5, 6, 4, 3]

def checkout(row, col):
    if row<0 or row>=N or col<0 or col>=M:
        return True
    return False

def move_dice(d):
    # RIGHT DOWN LEFT UP
    if d==0: # RIGHT
        # left top right bottom = bottom left top right
        dice[4], dice[1], dice[5], dice[3] = dice[3], dice[4], dice[1], dice[5]
    elif d==1: # DOWN
        # up top down bottom = bottom up top down
        dice[0], dice[1], dice[2], dice[3] = dice[3], dice[0], dice[1], dice[2]
    elif d==2: # LEFT
        # left top right bottom = top right bottom left
        dice[4], dice[1], dice[5], dice[3] = dice[1], dice[5], dice[3], dice[4]
    elif d==3: # UP
        # up top down bottom = top down bottom up
        dice[0], dice[1], dice[2], dice[3] = dice[1], dice[2], dice[3], dice[0]

def getgrade():
    for i in range(N):
        for j in range(M):
            if visited[i][j] == True:
                continue

            queue = deque([])
            queue.append((i, j))
            update = deque([])
            update.append((i, j))
            visited[i][j] = True

            cnt = 1
            num = board[i][j]

            while queue:
                row, col = queue.popleft()
                for k in range(4):
                    drow, dcol = row+dx[k], col+dy[k]
                    if not checkout(drow, dcol) and not visited[drow][dcol] and board[drow][dcol] == num:
                        cnt += 1
                        visited[drow][dcol] = True
                        queue.append((drow, dcol))
                        update.append((drow, dcol))

            while update:
                row, col = update.popleft()
                grade[row][col] = num*cnt

def simulate():
    global answer, now_dir, x_pos, y_pos
    for i in range(K):
        drow, dcol = x_pos+dx[now_dir], y_pos+dy[now_dir]
        if checkout(drow, dcol):
            now_dir = (now_dir+2)%4
            drow, dcol = x_pos+dx[now_dir], y_pos+dy[now_dir]
        move_dice(now_dir)

        answer += grade[drow][dcol]
        if dice[3] > board[drow][dcol]:
            now_dir = (now_dir+1)%4
        elif dice[3] < board[drow][dcol]:
            now_dir = (now_dir-1)%4
        x_pos, y_pos = drow, dcol

N, M, K = map(int, input().split())
board = []
for _ in range(N):
    board.append(list(map(int, input().split())))
visited = [[False]*M for _ in range(N)]
grade = [[0]*M for _ in range(N)]
answer = 0
x_pos, y_pos, now_dir = 0, 0, 0
getgrade()
simulate()
print(answer)
