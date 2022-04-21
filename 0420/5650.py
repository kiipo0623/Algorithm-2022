from collections import deque
#dir = up right down left
drow = [-1, 0, 1, 0]
dcol = [0, 1, 0, -1]

def do_move(row, col, dir):
    while graph[row][col] == 0:
        nrow = row + drow[dir]
        ncol = col + dcol[dir]
        row, col = nrow, ncol
    return [row, col, dir] # 0이 아닌 곳

def turn_wall(row, col, dir):
    if graph[row][col] == 1:
        if dir == 0 or dir == 1:
            return (dir+2)%4
        elif dir == 3:
            return 0
        elif dir == 2:
            return 1
    elif graph[row][col] == 2:
        if dir == 1 or dir == 2:
            return (dir+2)%4
        elif dir == 0:
            return 1
        elif dir == 3:
            return 2
    elif graph[row][col] == 3:
        if dir == 2 or dir == 3:
            return (dir+2)%4

    elif graph[row][col] == 4:
    elif graph[row][col] == 5:
        return (dir+2)%5

def wormhall(row, col, dir):


def do_simulation(row, col, dir):
    q = deque()
    q.append([row, col, dir])
    grade = 0
    while q:
        nrow, ncol, ndir = q.popleft()
        # 종료 조건 : 블랙홀
        if graph[nrow][ncol] == -1:
            return grade
        newrow, newcol, newdir = do_move(nrow, ncol, ndir)
        # 종료조건 : 처음 출발 지점
        if min(nrow, newrow)<=row<=max(nrow, newrow) and min(ncol, newcol)<=col<=max(ncol, newcol):
            return grade
        if graph[newrow][newcol] in [1, 2, 3, 4, 5]: # 벽
            grade += 1
            turn_wall(newrow, newcol, newdir)
        elif graph[newrow][newcol] in [6,7, 8, 9, 10]: #웜홀
            wormhall(newrow, newcol, newdir)




def make_candidate():
    global min_value
    for i in range(N):
        for j in range(N):
            for k in range(4):
                if graph[i][j] == 0:
                    min_value = min(min_value, do_simulation(i, j, k) )

T = int(input())
for i in range(T):
    N = int(input())
    min_value = int(1e9)
    graph = []
    for j in range(N):
        graph.append(list(map(int, input().split())))
