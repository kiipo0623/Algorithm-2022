from collections import deque
# 남 동 북 서
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

n, m, z = map(int, input().split())
arr = [[*map(int, input().split())] for _ in range(n)]

# 플러드 필
score = [[0]*m for _ in range(n)]
visit = [[0]*m for _ in range(n)]
for i in range(n):
    for j in range(m):
        if not visit[i][j]:
            q = deque([[i, j]])
            visit[i][j] = 1
            val = 1
            coordinate = [(i, j)]
            while q:
                x, y = q.popleft()
                for k in range(4):
                    nx, ny = x + dx[k], y + dy[k]
                    if 0 <= nx < n and 0 <= ny < m and not visit[nx][ny] and arr[x][y] == arr[nx][ny]:
                        visit[nx][ny] = 1
                        val += 1
                        coordinate.append((nx, ny))
                        q.append([nx, ny])
            for x, y in coordinate:
                score[x][y] = arr[x][y]*val

dice = [2, 1, 5, 6, 4, 3] # 전개도
down = [0, 6, 5, 4, 3, 2, 1]
ans = 0
arrow = 0 # 0:오른쪽 1:아래 2:왼쪽 3:위 # 전개도는 반대로 움직임
x, y = 0, 0
nx, ny = 0, 0
for _ in range(z):
    x, y = nx, ny
    nx, ny = x+dx[arrow], y+dy[arrow]
    if not (0<=nx<n and 0<=ny<m):
        arrow = (arrow+2)%4
        nx, ny = x + dx[arrow], y+dy[arrow]
    ans += score[nx][ny]

    if arrow == 0: #오른쪽
        dice[4], dice[1], dice[5], dice[3] = dice[3],dice[4], dice[1], dice[5]


    # 방향 변화
    if dice[3] > arr[nx][ny]:
        arrow = (arrow+1)%4
    if dice[3] < arr[nx][ny]:
        arrow = (arrow+3)%4
