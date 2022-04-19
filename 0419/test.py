from collections import deque

# 이동은 6가지 방향으로 가능하지만 작은 곳에서 시작하면 위쪽은 볼 필요가 없어서 4방향만 확인하면 된다
dx = [0, 1, 1, 0]
dy = [1, 1, 0, -1]

tc = int(input())
board = [[0]*141 for _ in range(141)]
num_loc = [()]
visited = [[0]*141 for _ in range(141)]
visited_num = 1

def solv(t):
    a, b = map(int, input().split())
    print('#%d %d'%(t, bfs(min(a, b), max(a, b))))

def bfs(a, b):
    global visited
    sx, sy = num_loc[a]
    ex, ey = num_loc[b]

    q = deque([(sx, sy, 0)])
    visited[sx][sy] = visited_num

    while q:
        x, y, cnt = q.pop()
        if x == ex and y == ey:
            return cnt

        for d in range(4):
            nx = x + dx[d]
            ny = y + dy[d]

            if point_validator(nx, ny, ex, ey):
                visited[nx][ny] = visited_num
                q.appendleft((nx, ny, cnt+1))

def point_validator(x, y, ex, ey):
    if x<0 or y<0 or x>ex or y>141:
        return False
    elif board[x][y] == 0:
        return False
    elif visited[x][y] == visited_num:
        return False
    return True

def init_board():
    global board
    num = 1
    for x in range(141):
        for y in range(x+1):
            board[x][y] = num
            num_loc.append((x, y))
            if num == 10000:
                return
            num += 1
    print(num)

init_board()
for t in range(1, tc+1):
    visited_num += 1
    solv(t)

print(visited)
print(num_loc)