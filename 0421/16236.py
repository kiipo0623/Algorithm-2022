from collections import deque

N = int(input())
graph = []

dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]

def nearest(start, size):
    answer = []
    minmove = -1
    queue = deque()
    queue.append([start[0], start[1], 0])
    visit = [[False] * N for _ in range(N)]
    visit[start[0]][start[1]] = True

    while queue:
        row, col, cnt = queue.popleft()

        if 0 < graph[row][col] < size:
            if minmove == -1:
                minmove = cnt
                answer.append((row, col, cnt))
            elif minmove == cnt:
                answer.append((row, col, cnt))
            else:
                break

        for i in range(4):
            arow, acol = row + dx[i], col + dy[i]
            if 0 <= arow < N and 0 <= acol < N and visit[arow][acol] == False and graph[arow][acol] <= size:
                queue.append([arow, acol, cnt + 1])
                visit[arow][acol] = True

    return answer

def dest(start, size):
    move = nearest(start, size)
    if len(move) == 0:
        return []
    elif len(move) == 1:
        return move[0]
    else:
        move = sorted(move, key=lambda x:(x[0], x[1]))
        return move[0]

def simulate():
    global graph
    time = 0
    size = 2
    eaten = 0
    pos = start

    while True:
        value = dest(pos, size)
        if len(value) == 0:
            return time

        else:
            row, col, cnt = value
            time += cnt

            eaten += 1
            if eaten == size:
                size += 1
                eaten = 0

            graph[pos[0]][pos[1]] = 0 # 이전 위치 정리

            pos = [row, col] # 상어 위치 갱신

INF = int(1e9)
for i in range(N):
    data = list(map(int, input().split()))
    for j in range(N):
        if data[j] == 9:
            start = [i, j]
    graph.append(data)

graph[start[0]][start[1]] = 0
print(simulate())