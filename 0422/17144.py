from copy import deepcopy
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def dirty(g):
    minus_graph, plus_graph, new_graph = [[0]*C for _ in range(R)], [[0]*C for _ in range(R)], [[0]*C for _ in range(R)]

    for i in range(R):
        for j in range(C):
            if g[i][j] > 0:
                move_dirt = g[i][j]//5
                cnt = 0
                for k in range(4):
                    nrow, ncol = i+dx[k], j+dy[k]
                    if 0<=nrow<R and 0<=ncol<C and g[nrow][ncol] != -1:
                        plus_graph[nrow][ncol] += move_dirt
                        cnt += 1
                minus_graph[i][j] = g[i][j]-(move_dirt*cnt)

    for i in range(R):
        for j in range(C):
            new_graph[i][j] = minus_graph[i][j]+plus_graph[i][j]
    return new_graph

def move_right(graph, row, startcol, endcol, item):
    now = item
    next = graph[row][startcol]
    graph[row][startcol] = now

    for i in range(startcol, endcol):
        now = next
        next = graph[row][i+1]
        graph[row][i+1]=now

    return (graph, next)

def move_up(graph, col, startrow, endrow, item):
    now = item
    next = graph[startrow-1][col]
    graph[startrow-1][col] = now

    for i in range(startrow-1, endrow, -1):
        now = next
        next = graph[i - 1][col]
        graph[i - 1][col] = now

    return (graph, next)

def move_down(graph, col, startrow, endrow, item):
    now = item
    next = graph[startrow+1][col]
    graph[startrow+1][col] = now

    for i in range(startrow+1, endrow):
        now = next
        next = graph[i + 1][col]
        graph[i + 1][col] = now
    return (graph, next)

def move_left(graph, row, startcol, endcol, item):
    now = item
    next = graph[row][startcol-1]
    graph[row][startcol-1] = now

    for i in range(startcol-1, endcol, -1):
        now = next
        next = graph[row][i-1]
        graph[row][i-1] = now

    return (graph, next)

def cleaner_up(g, pos):
    row, col = pos
    g[row][col] = 0
    AR, item = move_right(g, row, 0, C-1, 0)
    AU, item = move_up(AR, C-1, row, 0, item)
    AL, item = move_left(AU, 0, C-1, 0, item)
    AD, item = move_down(AL, 0, 0, row, item)
    AD[row][col] = -1
    return AD

def cleaner_down(g, pos):
    row, col = pos
    g[row][col] = 0
    AR, item = move_right(g, row, 0, C-1, 0)
    AD, item = move_down(g, C-1, row, R-1, item)
    AL, item = move_left(g, R-1, C-1, 0, item)
    AU, item = move_up(g, 0, R-1, row, item)
    AU[row][col] = -1
    return AU

def simulate():
    global graph
    for _ in range(T):
        dirtygraph = dirty(graph)
        upgraph = cleaner_up(dirtygraph, cleaner[0])
        downgraph = cleaner_down(upgraph, cleaner[1])
        graph = deepcopy(downgraph)

R, C, T = map(int, input().split())
graph = []
for _ in range(R):
    graph.append(list(map(int,input().split())))

cleaner = []
for i in range(2, R):
    if graph[i][0] == -1:
        cleaner.append((i, 0))

simulate()

answer = 0
for i in range(R):
    for j in range(C):
        if graph[i][j]>0:
            answer += graph[i][j]

print(answer)