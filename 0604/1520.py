import sys
input = sys.stdin.readline

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

def dfs(x, y):
    if x == m-1 and y == n-1:
        return 1
    if c[x][y] != -1: # 방문 한 경우
        return c[x][y]

    c[x][y] = 0
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if 0 <= nx < m and 0 <= ny < n: # 네 방향에 대해서
            if a[nx][ny] < a[x][y]: # 다른 곳에서 오는 걸 다 합친다
                c[x][y] += dfs(nx, ny)



m, n = map(int, input().split())
a = [list(map(int, input().split())) for _ in range(m)]
c = [[-1]*n for _ in range(m)]

print(dfs(0, 0))