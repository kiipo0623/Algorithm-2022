from collections import deque
N, M = int(input()), int(input())
link = [[] for _ in range(N+1)]
matrix = [[0]*(N+1) for _ in range(N+1)]
indegree = [0 for _ in range(N+1)]

for i in range(M):
    a, b, c = map(int, input().split())
    link[b].append((a, c))
    indegree[a] += 1

queue = deque()
for i in range(1, N+1):
    if indegree[i] == 0:
        queue.append(i)

while queue:
    now = queue.popleft()
    for next, needs in link[now]:
        if matrix[now].count(0) == N+1: #진입 차수 없는 기본 부품
            matrix[next][now] += needs
        else:
            for i in range(1, N+1):
                matrix[next][i] += matrix[now][i] * needs
        indegree[next] -= 1
        if indegree[next] == 0:
            queue.append(next)

for i in enumerate(matrix[N]):
    if i[1] > 0:
        print(i[0], i[1])