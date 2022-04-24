def notcircle2(graph, now):
    for i in range(now[0] - 2, -1, -1):
        graph[i + 1][0] = graph[i][0]
    for i in range(1, C):
        graph[0][i - 1] = graph[0][i]
    for i in range(1, now[0] + 1):
        graph[i - 1][-1] = graph[i][-1]
    for i in range(C - 2, 0, -1):
        graph[now[0]][i + 1] = graph[now[0]][i]
    graph[now[0]][1] = 0
    return graph

R, C = 3, 5
n = [2, 3]
graph = [[1,2,3,4,5],
 [6,7,8,9,10],
 [11,12,13,14,15]]
# print(notcircle1(graph, n))
print(notcircle2(graph, n))
