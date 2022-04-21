# 우 상 좌 하 // dx dy 바뀜
dx = [1, 0, -1, 0]
dy = [0, -1, 0, 1]

def make_dir(d, g):
    dir_list = [d]
    for i in range(g):
        tmp = []
        for j in range(len(dir_list)):
            tmp.append((dir_list[-j-1]+1)%4)
        dir_list.extend(tmp)
    return dir_list

def mark_graph(x, y, dirlist):
    global graph
    graph[y][x] = 1
    for dir in dirlist:
        nx, ny = x+dx[dir], y+dy[dir]
        graph[ny][nx] = 1
        x, y = nx, ny

def count_graph():
    cnt = 0
    for i in range(100):
        for j in range(100):
            if graph[i][j] and graph[i][j+1] and graph[i+1][j] and graph[i+1][j+1]:
                cnt += 1
    return cnt

N = int(input())
graph = [[0]*101 for _ in range(101)]
for _ in range(N):
    x, y, d, g = map(int, input().split())
    direction_list = make_dir(d, g)
    mark_graph(x, y, direction_list)

sol = count_graph()
print(sol)