from collections import defaultdict, deque
def bfs(graph, info, start):
    if info[start] == 0:
        return True

    queue = deque([start])

    while queue:
        now = queue.popleft()
        for node in graph[now]:
            if info[node] == 0:
                return True
            queue.append(node)

    return False

def checker(visited, info):
    cnt = 1
    sheepcount = 1
    for v in visited[1:]:
        if info[v] == 1: # 늑대면
            cnt -= 1
        else: # 양이면
            cnt += 1
            sheepcount += 1
        if cnt <= 0:
            break
    return sheepcount


def bt(visited, info):
    global tosearch, answer
    if len(visited) == len(tosearch):
        # print(visited)
        answer = max(answer, checker(visited, info))
        return

    for now in visited:
        for node in graph[now]:
            if node in tosearch and node not in visited:
                visited.append(node)
                bt(visited, info)
                visited.pop()


def solution(info, edges):
    global graph, tosearch, answer
    answer = 0
    graph = defaultdict(list)
    notsearch = []

    for p, s in edges:
        graph[p].append(s)

    for i in range(len(info)):
        if not bfs(graph, info, i): # False
            notsearch.append(i)

    tosearch = [i for i in range(len(info)) if i not in notsearch]
    bt([0], info)
    return answer

print(solution(
[0,0,1,1,1,0,1,0,1,0,1,1],
[[0,1],[1,2],[1,4],[0,8],[8,7],[9,10],[9,11],[4,3],[6,5],[4,6],[8,9]]
))

print(solution(
[0,1,0,1,1,0,1,0,0,1,0],
[[0,1],[0,2],[1,3],[1,4],[2,5],[2,6],[3,7],[4,8],[6,9],[9,10]]
))