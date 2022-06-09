# Prim 알고리즘으로 : 선택되지 않은 node 중 가장 가까운 곳 선택
# 음수여도 가능한지
# 1:15

V, E = map(int, input().split())

graph = [[] for _ in range(V+1)]

selected = [1]
flag = [True]*2 + [False]*(V-1)
answer = 0

for _ in range(E):
    A, B, C = map(int, input().split())
    graph[A].append((B, C))
    graph[B].append((A, C))

for _ in range(V-1):
    minL, nodeidx = int(1e9), -1
    for s in selected:
        for node, cost in graph[s]:
            if not flag[node] and minL > cost:
                minL, nodeidx = cost, node
    selected.append(nodeidx)
    flag[nodeidx] = True
    answer += minL

print(answer)