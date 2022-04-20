from collections import deque
from copy import deepcopy
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def count_distance(queue):
    sum_ = 0
    for h in home:
        temp = int(1e9)
        for c in queue:
            temp = min(temp, abs(h[0]-c[0]) + abs(h[1]-c[1]))
        sum_ += temp
    return sum_

# 중복 처리가 안되는 combination
def dfs(depth, q):
    global min_value
    if depth == M:
        min_value = min(min_value, count_distance(list(q)))

    if len(q) == 0:
        start = 0
    else:
        start = chicken.index(q[-1])+1

    for i in range(start, len(chicken)):
        q.append(chicken[i])
        dfs(depth+1, q)
        q.pop()


N, M = map(int, input().split())
graph = []
home = []
chicken = []
min_value = int(1e9)

for i in range(N):
    data = list(map(int, input().split()))
    for j in range(N):
        if data[j] == 1:
            home.append((i, j))
        elif data[j] == 2:
            chicken.append((i, j))
    graph.append(data)

dfs(0, deque())

print(min_value)

