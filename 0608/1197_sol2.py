# Prim 알고리즘으로 : 선택되지 않은 node 중 가장 가까운 곳 선택
# 음수여도 가능한지
# 1:15
INF = int(1e9)

V, E = map(int, input().split())

graph = [[INF]*(V+1) for _ in range(V+1)]

selected = [1]
unselected = [i for i in range(2, V+1)]
answer = 0

for _ in range(E):
    A, B, C = map(int, input().split())
    graph[A][B] = C
    graph[B][A] = C

for _ in range(V-1):
    minL, nodeidx = int(1e9), -1
    for s in selected:
        for un in unselected:
            if minL > graph[s][un]:
                minL = graph[s][un]
                nodeidx = un

    selected.append(nodeidx)
    unselected.remove(nodeidx)

    answer += minL

print(answer)