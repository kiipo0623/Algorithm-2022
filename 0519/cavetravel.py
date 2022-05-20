from collections import deque
from copy import deepcopy
def backtracking(tovisit, ordercheck, cnt, visited):
    print(visited)
    print(cnt)
    global N, turn, graph
    if cnt == N:
        return True

    length = len(tovisit)
    for _ in range(length):
        now = tovisit.popleft()
        visited.append(now)

        if now in turn.keys():
            oc, tv = deepcopy(ordercheck), deepcopy(tovisit)
            oc[turn[now]][1] = True # 시간초과시 turn 줄이기
            if oc[turn[now]] == [True, True]:
                tv.append(turn[now])
                del oc[turn[now]]
                backtracking(tv, oc, cnt+1, visited)

        for next in graph[now]:
            if ordercheck.get(next, 0): # 후방문노드
                oc, tv = deepcopy(ordercheck), deepcopy(tovisit)
                oc[next][0] = True # 이게 계속 가는게 아니지 ?
                if oc[next] == [True, True]:
                    tv.append(next)
                    del oc[next]
                    backtracking(tv, oc, cnt+1, visited)

            elif next not in visited:
                tovisit.append(next)
                backtracking(tovisit, ordercheck, cnt+1, visited)
                tovisit.pop()

        visited.pop()
        tovisit.append(now)



def solution(n, path, order):
    global N, turn, graph
    N = n
    answer = True
    graph = [[] for _ in range(n)]
    for p in path:
        graph[p[0]].append(p[1])
        graph[p[1]].append(p[0])
    chk = {o[1]:[False, False] for o in order}
    turn = {o[0]:o[1] for o in order}
    q = deque()
    q.append(0)
    return backtracking(q, chk, 0, [])

print(solution(
    9, [[0,1],[0,3],[0,7],[8,1],[3,6],[1,2],[4,7],[7,5]], [[8,5],[6,7],[4,1]]
))