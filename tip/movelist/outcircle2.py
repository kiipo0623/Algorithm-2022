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

def notcircle(graph):
    R, C = len(graph), len(graph[0])
    # 위
    temp = graph[1][0]
    for i in range(1, C-2):
        graph[0][i] = graph[0][i+1]
    # 왼
    for i in range(R-2, 0, -1):
        graph[i][0] = graph[i-1][0]
    # 아래
    for i in range(C-1, 0, -1):
        graph[R-1][i] = graph[R-1][i-1]
    # 오른
    for i in range(0, R-2):
        graph[i][C-1] = graph[i+1][C-1]
    graph[0][0] = temp

def circle(graph):
    R, C = len(graph), len(graph[0])
    temp = graph[0][C-2]
    # 위
    for i in range(C-2, 0, -1):
        graph[0][i] = graph[0][i-1]
    # 왼쪽
    for i in range(0, R-1):
        graph[i][0] = graph[i+1][0]
    # 아래
    for i in range(0, C - 2):
        graph[R - 1][i] = graph[R - 1][i + 1]
    # 오른쪽
    for i in range(R-1, 0, -1):
        graph[i][C-1] = graph[i-1][C-1]
    graph[0][C-1] = temp
    return graph


g = [[1,2,3,4,5],
 [6,7,8,9,10],
 [11,12,13,14,15]]
print(notcircle(g))
