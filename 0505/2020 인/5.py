from collections import deque
def bfs(board, cannotgo, order_dict):
    queue = deque([])
    visited = [False]*len(board)
    queue.append(0)

    while queue:
        now = queue.popleft()
        visited[now] = True
        for node in board[now]:
            if visited[node]:
                continue
            if node in cannotgo:
                continue
            if node in order_dict.keys():
                cannotgo.remove(order_dict[node])
                queue.append(order_dict[node])
            queue.append(node)

    if all(visited):
        return True
    else:
        return False


def solution(n, path, order):
    board = [[] for _ in range(n)]

    for p in path:
        board[p[0]].append(p[1])
        board[p[1]].append(p[0])

    cannotgo = []
    order_dict = dict()
    for o in order:
        order_dict[o[0]] = o[1]
        cannotgo.append(o[1])

    return bfs(board, cannotgo, order_dict)

print(solution(
    9, [[0,1],[0,3],[0,7],[8,1],[3,6],[1,2],[4,7],[7,5]], [[8,5],[6,7],[4,1]]
))