from collections import deque
from copy import deepcopy

def game(newladders):
    temp = deepcopy(graph)
    for newlad in newladders:
        row, col = newlad
        temp[row][col] = 1

    for i in range(1,N+1):
        nrow, ncol = 1, i
        while nrow<=H:
            if temp[nrow][ncol] == 1:
                ncol += 1
                nrow += 1
            elif temp[nrow][ncol-1] == 1:
                ncol -= 1
                nrow += 1
            else:
                nrow += 1
        if ncol != i:
            return False
    return True
    # 새 사다리 설치
    # 라인의 수만큼 반복문
    # 안에서 while문 사용하여 결과 확인

def dfs(depth, maxdepth, q):
    global answer, candidate
    if depth == maxdepth:
        candidate.add(tuple(sorted(q)))
        return

    for i in range(1, H+1):
        for j in range(1, N):
            if [i,j] in ladder or [i,j-1] in ladder or [i, j+1] in ladder:
                continue
            if (i,j) in q:
                continue
            q.append((i, j))
            dfs(depth+1, maxdepth, q)
            q.pop()


N, M, H = map(int, input().split())
graph = [[0]*(N+1) for _ in range(H+1)]
ladder = []

answer = -1

for _ in range(M):
    a, b = map(int, input().split())
    graph[a][b] = 1
    ladder.append([a, b])


for i in range(0, 4):
    if answer != -1:
        break
    queue = deque()
    candidate = set()
    dfs(0, i, queue)

    for c in candidate: # 한번에 놓는 사다리의 개수
        if game(c):
            answer = len(c)
            break

print(answer)


