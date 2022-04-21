from collections import deque
N, L, R = map(int, input().split())
popularity = [list(map(int, input().split())) for _ in range(N)]
day = 0
graph = dict()

def check(value, input, x, y):
    if (input >= L) and (input <= R):
        value.append((x, y))

def border(i, j):
    value = []
    if i-1 >= 0:
        top = abs(popularity[i-1][j]-popularity[i][j])
        check(value, top, i-1, j)
    if i+1 < N:
        bottom = abs(popularity[i + 1][j] - popularity[i][j])
        check(value, bottom, i + 1, j)
    if j - 1 >= 0:
        left = abs(popularity[i][j - 1] - popularity[i][j])
        check(value, left, i, j - 1)
    if j + 1 < N:
        right = abs(popularity[i][j + 1] - popularity[i][j])
        check(value, right, i, j + 1)
    if value:
        graph[(i, j)] = value

def bfs(start):
    visit = list()
    queue = deque()
    queue.append(start)
    while queue:
        enqueue = queue.popleft()
        if enqueue not in visit:
            visit.append(enqueue)
            queue.extend(graph[enqueue])
    return visit

while True:
    for i in range(N):
        for j in range(N):
            border(i, j)

    if not graph:
        break

    while graph:
        movement = bfs(list(graph.keys())[0])
        sum = 0

        for move in movement:
            sum += popularity[move[0]][move[1]]
        result = int(sum/len(movement))

        for move in movement:
            popularity[move[0]][move[1]] = result
            del(graph[move])
    day += 1

print(day)