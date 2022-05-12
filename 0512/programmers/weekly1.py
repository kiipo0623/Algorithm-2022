from collections import deque
# 전력망을 둘로 나누기
def dfs(disconnect, start, n):
    global graph
    visited = [False]*(n+1)
    visited[start] = True
    queue = deque([start])

    while queue:
        now = queue.popleft()
        for node in graph[now]:
            if not visited[node] and ([now, node] != disconnect) and ([node, now] != disconnect):
                visited[node] = True
                queue.append(node)

    return visited.count(True)


def solution(n, wires):
    global graph
    answer = int(1e9)
    graph = [[] for _ in range(n+1)]

    for wire in wires:
        v1, v2 = wire
        graph[v1].append(v2)
        graph[v2].append(v1)
    print(graph)

    for wire in wires:
        print(wire)
        n1 = dfs(wire, wire[0], n)
        n2 = dfs(wire, wire[1], n)
        answer = min(answer, abs(n1-n2))
        if n%2==1 and answer == 1: return answer
        if n%2==0 and answer == 0:return answer

    return answer

print(solution(
    9, [[1,3],[2,3],[3,4],[4,5],[4,6],[4,7],[7,8],[7,9]]
))