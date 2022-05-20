# 시간 문제 시 deque 사용
# tovisit을 queue사용 /visited와 lock을 리스트로
import sys
sys.setrecursionlimit(10**6)
flag = False
def backtrack(tv, v, l):
    global N, turn, graph, flag
    if all(v):
        flag = True
        return

    for node in tv:
        if node not in l: # 예외조건 확인
            tv.remove(node)
            v.append(node)

            if node in turn.keys() and turn[node] in l: # 예외조건 처리
                l.remove(turn[node])

            for new in graph[node]: # 예외조건 확인 안하고 추가
                if new not in v:
                    tv.append(new)
            backtrack(tv, v, l)


def solution(n, path, order):
    global N, turn, graph, flag
    N = n
    graph = [[] for _ in range(n)]
    for p in path:
        graph[p[0]].append(p[1])
        graph[p[1]].append(p[0])

    turn = {o[0]:o[1] for o in order}
    lock = [o[1] for o in order]
    backtrack([0], [], lock)
    if flag:
        return True
    else:
        return False

print(solution(
    9, [[0,1],[0,3],[0,7],[8,1],[3,6],[1,2],[4,7],[7,5]], [[8,5],[6,7],[4,1]]
))