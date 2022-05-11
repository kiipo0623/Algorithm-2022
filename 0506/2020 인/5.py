from collections import deque
def bfs(tree, n):
    queue = deque([])
    queue.append(0)
    visited = [False]*n
    visitflag = {node:False for node in afterflag.keys()}

    while queue:
        now = queue.popleft()
        if not visited[now]:
            visited[now] = True

            if not beforeflag[now]:
                beforeflag[now] = True
                afterflag[order_dict[now]] = True

                if visitflag[order_dict[now]] == True:
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

# print(solution(

# print(solution(
#     9, [[8,1],[0,1],[1,2],[0,7],[4,7],[0,3],[7,5],[3,6]], [[4,1],[5,2]]
# ))
print(solution(
    9, [[0,1],[0,3],[0,7],[8,1],[3,6],[1,2],[4,7],[7,5]], [[4,1],[8,7],[6,5]]
))