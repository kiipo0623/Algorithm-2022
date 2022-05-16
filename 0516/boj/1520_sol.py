dx = [1, -1, 0, 0]
dy = [0, 0, -1, 1]

def dfs(x, y):
    if x == M-1 and y ==N-1:
        return 1
    if c[x][y] != -1: # 방문한 경우
        return c[x][y]
    c[x][y] = 0 # 0으로 재설정
    for i in range(4): # 방문하지 않은 경우
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < M and 0 <= ny < N:
            if a[nx][ny] < a[x][y]:
                c[x][y] += dfs(nx, ny)
    return c[x][y]


M, N = map(int, input().split())
a = [list(map(int, input().split())) for _ in range(M)]
c = [[-1]*N for _ in range(M)]
print(dfs(0, 0))