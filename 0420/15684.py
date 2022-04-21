from copy import deepcopy
def do_simulation(g):
    for i in range(1, N+1):
        now = i
        for j in range(1, H+1):
            if g[j][now] == 1:
                now += 1
            elif g[j][now-1] == 1:
                now -= 1
        if now != i:
            return False
    return True

def make_graph(queue):
    temp_graph = deepcopy(graph)
    for sero, garo in queue:
        temp_graph[sero][garo] = True
    if do_simulation(temp_graph):
        return True
    else:
        return False

def make_combination(maxdepth, queue):
    global answer
    if answer != 4:
        return
    if len(queue) == maxdepth:
        if sorted(queue) in already_check:
            return

        already_check.append(sorted(queue))
        if make_graph(queue):
            answer = maxdepth
            return
        else:
            return

    for i in range(1, H+1):
        for j in range(1, N):
            if (i, j) in origin_ladder or (i, j-1) in origin_ladder or (i, j+1) in origin_ladder:
                continue
            if (i, j) in queue:
                continue
            queue.append((i, j))
            make_combination(maxdepth, queue)
            queue.pop()


N, M, H = map(int, input().split())
origin_ladder = []
graph = [[False]*(N+1) for _ in range(H+1)]
for _ in range(M):
    a, b = map(int, input().split())
    origin_ladder.append((a, b))
    graph[a][b] = True

answer = 4
for i in range(0, 4):
    already_check = []
    make_combination(i, [])
    if answer != 4:
        break

if answer<4:
    print(answer)
else:
    print(-1)