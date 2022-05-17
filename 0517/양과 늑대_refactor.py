def dfs(now, sheep, wolf, path, info):
    global answer, tree
    if info[now] == 1:
        wolf += 1
    else:
        sheep += 1

    if wolf >= sheep:
        return

    answer = max(answer, sheep)
    path.extend(tree[now])

    for p in path:
        tmp = path[:]
        tmp.remove(p)
        dfs(p, sheep, wolf, tmp, info)


def solution(info, edges):
    global answer, tree
    answer = 0
    tree = [[] for _ in range(len(info))]

    for edge in edges:
        pa, so = edge
        tree[pa].append(so)

    dfs(0, 0, 0, [], info)
    return answer

print(solution(
[0,0,1,1,1,0,1,0,1,0,1,1],
[[0,1],[1,2],[1,4],[0,8],[8,7],[9,10],[9,11],[4,3],[6,5],[4,6],[8,9]]
))

print(solution(
[0,1,0,1,1,0,1,0,0,1,0],
[[0,1],[0,2],[1,3],[1,4],[2,5],[2,6],[3,7],[4,8],[6,9],[9,10]]
))