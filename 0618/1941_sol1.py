from itertools import combinations
from collections import deque

graph = []
direction = [(-1, 0), (1, 0), (0, -1), (0, 1)]
position = [(i, j) for i in range(5) for j in range(5)]
combs = list(combinations(position, 7))
answer = 0

for _ in range(5):
    graph.append(list(input()))

def checkDaSom(givenComb):
    daSom = 0
    for x, y in givenComb:
        if graph[x][y] == 'S':
            daSom += 1

    if daSom >= 4:
        return True
    else:
        return False

def checkAdjacent(givenComb):
    visited = [False]*7
    q = deque()
    q.append(givenComb[0])
    visited[0] = True

    while q:
        x, y = q.popleft()
        for d in direction:
            nx, ny = x+d[0], y+d[1]
            if (nx, ny) in givenComb:
                nextIdx = givenComb.index((nx, ny))
                if not visited[nextIdx]:
                    visited[nextIdx] = True
                    q.append((nx, ny))

    if all(visited):
        return True
    else:
        return False

for comb in combs:
    if checkDaSom(comb) and checkAdjacent(comb):
        answer += 1

print(answer)
