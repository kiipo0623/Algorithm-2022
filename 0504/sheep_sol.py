def solution(info, edges):
    def nextNodes(v):
        temp = list()
        for e in edges:
            i, j = e
            if v == i:
                temp.append(j)
        return temp

    def dfs(sheep, wolf, current, path):
        if info[current]: # 늑대면
            wolf += 1
        else:
            sheep += 1

        # 늑대가 다 잡아먹음 종료
        if sheep <= wolf:
            return 0

        # 임시 변수에 값 갱신
        maxSheep = sheep

        for p in path: # 현재 방문한 노드에 대해
            for n in nextNodes(p): # 방문할 수 있는 노드들
                path.append(n)
                maxSheep = max(maxSheep, dfs(sheep, wolf, n, path))
                path.pop()

        return maxSheep

    answer = dfs(0, 0, 0, [0])
    return answer