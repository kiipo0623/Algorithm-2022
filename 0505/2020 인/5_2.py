from collections import deque
def solution(n, path, order):
    answer = True
    adj = {n: [] for n in range(n)}
    for s, e in path:
        adj[s].append(e)
        adj[e].append(s)

    precedeA = {}
    precedeB = {}

    for a, b in order:
        precedeA[a] = b # key : 먼저 방문 value : 나중에 방문
        precedeB[b] = a # key : 나중에 방문 value : 먼저 방문
        if b == 0:
            return False
        if a == 0:
            precedeA[0] = 0

    visited = [0]*n
    visited[0] = 1

    q = deque()
    q.append(0)

    while q:
        current = q.popleft()
        # 알고보니 아직 못가는 상태
        if current == precedeA.get(precedeB.get(current)):
            visited[current] = 2
        else:
            for neighbor in adj[current]:
                if visited[neighbor] == 0:
                    q.append(neighbor)
                    visited[neighbor] = 1

                    if precedeA.get(neighbor):  # 선행조건 일 때
                        if visited[precedeA[neighbor]] == 2:  # 이 선행조건을 필요로 하는 친구가 준비상태이면
                            q.append(precedeA[neighbor])  # 출발시킨다
                            visited[precedeA[neighbor]] = 1

                        precedeA[neighbor] = 0

    for i in visited:
        if i == 0:
            return False
    return answer
