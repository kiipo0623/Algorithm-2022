# arrive (도달O 이전X)
# visit (도달O 이전O)
# after (도달X 이전X)
# 이건 백트래킹이 아니라 dfs이다..
def backtracking(visited, tovisit, orderarrive, ordervisit, after):
    global N, graph, turn
    print(visited)
    if len(visited) == N:
        return True

    for node in tovisit:
        v, tv, oa,ov, a = visited[:], tovisit[:], orderarrive[:], ordervisit[:], after[:]
        v.append(node)
        tv.remove(node)

        if node in turn.keys():
            if turn[node] in a: # 도달, 이전 안함 > 여기를 통해서 이전 해결
                ov.append(turn[node])
                a.remove(turn[node])

            if turn[node] in oa: # 도달은 했는데 이전 안함
                tv.append(turn[node])
                oa.remove(turn[node])

        for new in graph[node]: # 연결된 그래프
            if new not in v: # 방문 안했으면
                if new in a: # 방문은 해결됐으니까
                    oa.append(new)
                    a.remove(new)
                    backtracking(v, tv, oa, ov, a)
                    oa.pop()
                    a.append(new)

                elif new in ov: # 방문은 해결됐을 때
                    tv.append(new)
                    ov.remove(new)
                    backtracking(v, tv, oa, ov, a)
                    tv.pop()
                    ov.append(new)

                else:
                    tv.append(new)
                    backtracking(v, tv, oa, ov, a)
                    tv.pop()


def solution(n, path, order):
    global N, graph, turn
    N = n
    answer = True

    graph = [[] for _ in range(n)]
    for p in path:
        graph[p[0]].append(p[1])
        graph[p[1]].append(p[0])

    turn = {o[0]: o[1] for o in order}
    after = [o[1] for o in order]
    if backtracking([], [0],[], [], after):
        return True
    else:
        return False


print(solution(
    9, [[0,1],[0,3],[0,7],[8,1],[3,6],[1,2],[4,7],[7,5]], [[8,5],[6,7],[4,1]]
))