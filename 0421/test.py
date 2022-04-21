
dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]

from collections import deque

def nearest(start, size):
    answer = []
    minmove = int(1e9)
    queue = deque()
    queue.append([start[0], start[1], 0])
    visit = [[False] * N for _ in range(N)]
    visit[start[0]][start[1]] = True
    while queue:
        row, col, cnt = queue.popleft()

        if 0 < graph[row][col] < size:
            if minmove == int(1e9):
                minmove = cnt
                answer.append((row, col))
            elif minmove == cnt:
                answer.append((row, col))
            else:
                break

        for i in range(4):
            arow, acol = row + dx[i], col + dy[i]
            if 0 <= arow < N and 0 <= acol < N and visit[arow][acol] == False and graph[arow][acol] <= size:
                queue.append([arow, acol, cnt + 1])
                visit[arow][acol] = True

    return answer

N = 10
graph = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 9, 1, 0], [1, 1, 1, 1, 1, 1, 1, 1, 1, 0], [1, 1, 1, 1, 1, 1, 1, 1, 1, 0], [1, 1, 1, 1, 1, 1, 1, 1, 1, 0], [1, 1, 1, 1, 1, 1, 1, 1, 1, 0], [1, 1, 1, 1, 1, 1, 1, 1, 1, 0], [1, 1, 1, 1, 1, 1, 1, 1, 1, 0]]

print(nearest([3,7], 2))
