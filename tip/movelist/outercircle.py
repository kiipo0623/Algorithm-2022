# 백준 17144
'''
[[1,2,3,4,5],
 [6,7,8,9,10],
 [11,12,13,14,15]
반시계방향
[[2,3,4,5,10],
 [1,7,8,9,15],
 [6,11,12,13,14]]
 시계방향
 [[6,1,2,3,4],
  [11,7,8,9,5],
  [12,13,14,15,10]]
'''
def clock(graph):
    R, C = len(graph), len(graph[0])
    # (0, 0) 부터 시작
    dx = [0, 1, 0, -1]
    dy = [1, 0, -1, 0]
    direct = 0
    startR, startC = 0, 0
    x, y = 0, 1
    before = graph[startR][startC]
    while True:
        nx, ny = x + dx[direct], y + dy[direct]
        if x==startR and y==startC:
            graph[startR][startC] = before
            break
        if nx<0 or nx>=R or ny<0 or ny>=C:
            direct += 1
            continue
        graph[x][y], before = before, graph[x][y]
        x, y = nx, ny
    return graph

def notclock(graph):
    R, C = len(graph), len(graph[0])
    dx = [1, 0, -1, 0]
    dy = [0, 1, 0, -1]
    startR, startC = 0, 0
    direct = 0
    x, y = 1, 0
    before = graph[startR][startC]

    while True:
        nx, ny = x + dx[direct], y + dy[direct]
        if x==startR and y==startC:
            graph[startR][startC] = before
            break
        if nx<0 or nx>=R or ny<0 or ny>=C:
            direct += 1
            continue
        graph[x][y], before = before, graph[x][y]
        x, y = nx, ny
    return graph

test = [[1,2,3,4,5],
 [6,7,8,9,10],
 [11,12,13,14,15]]

print(notclock(test))