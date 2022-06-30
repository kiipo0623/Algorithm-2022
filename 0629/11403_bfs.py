from collections import deque
def BFS(start):
    queue = deque()
    queue.append(start)
    answer = [0]*N

    while queue:
        now = queue.popleft()
        for i in range(N):
            if graph[now][i] and not answer[i]:
                queue.append(i)
                answer[i] = 1
    print(' '.join(map(str, answer)))


N = int(input())
graph = []
for _ in range(N):
    graph.append(list(map(int, input().split())))

for i in range(N):
    BFS(i)

