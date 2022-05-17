def solution(info, edges):
    tree = [[] for _ in range(len(info))]

    def dfs(sheep, wolf, current, path):
        if info[current]:
            wolf += 1
        else:
            sheep += 1

        if sheep <= wolf:
            return 0

        maxSheep = sheep

        for p in path:
            for node in tree[p]:
                if node not in path:
                    path.append(node)
                    maxSheep = max(maxSheep, dfs(sheep, wolf, node, path)) # 새로 추가되는 노드에 대해서 탐색 ?
                    path.pop()

        return maxSheep

    for edge in edges:
        par, son = edge
        tree[par].append(son)

    answer = dfs(0, 0, 0, [0])
    return answer

print(solution(
[0,0,1,1,1,0,1,0,1,0,1,1],
[[0,1],[1,2],[1,4],[0,8],[8,7],[9,10],[9,11],[4,3],[6,5],[4,6],[8,9]]
))

print(solution(
[0,1,0,1,1,0,1,0,0,1,0],
[[0,1],[0,2],[1,3],[1,4],[2,5],[2,6],[3,7],[4,8],[6,9],[9,10]]
))