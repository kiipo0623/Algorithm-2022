from collections import deque
def bfs(tree, n):
    queue = deque([])
    queue.append(0)
    visited = [False]*n
    visitflag = {node:False for node in afterflag.keys()} # 거기에 도달한거
    print(visitflag)

    while queue:
        now = queue.popleft()
        if not visited[now]: # 방문 안했으면
            visited[now] = True

            if not beforeflag[now]: # 전순위 노드면
                beforeflag[now] = True
                afterflag[order_dict[now]] = True

                if visitflag[order_dict[now]] == True: # 후순위 노드 방문 가능하면 추가 : 이거 안하면 그냥 이미 넘어간것(bfs)
                    queue.append(order_dict[now])

            for node in tree[now]:
                if afterflag[node]: # 방문 가능
                    queue.append(node)
                else:
                    visitflag[node] = True
    if all(visited):
        return True
    else:
        return False

def solution(n, path, order):
    global order_dict, beforeflag, afterflag
    tree = [[] for _ in range(n)]
    for p in path:
        tree[p[0]].append(p[1])
        tree[p[1]].append(p[0])

    order_dict = {}
    beforeflag = {i:True for i in range(n)}
    afterflag = {i:True for i in range(n)}
    for o in order:
        order_dict[o[0]] = o[1]
        beforeflag[o[0]] = False
        afterflag[o[1]] = False

    beforeflag[0] = True

    return bfs(tree, n)


print(solution(
    9, [[0,1],[0,3],[0,7],[8,1],[3,6],[1,2],[4,7],[7,5]], [[4,1],[8,7],[6,5]]
))