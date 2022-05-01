from collections import deque

def bfs(start, b):
    queue = deque([])
    queue.append(start)
    visit = [False]*(N+1)
    visit[start] = True
    while queue:
        now = queue.popleft()
        for city in lst:
            if not visit[city] and b[now][city]:
                visit[city] = True
                queue.append(city)
    return visit

def garimandering(select): # 1 2번 포함 :
    myteam = select
    otherteam = [i for i in range(1, N+1) if i not in select]

    tmp = [a[:] for a in connect]

    for m in myteam:
        for o in otherteam:
            tmp[m][o] = False
            tmp[o][m] = False

    mvisit, ovisit = bfs(myteam[0], tmp), bfs(otherteam[0], tmp)

    msum, osum = 0, 0
    for p in myteam:
        msum += people[p]
        if mvisit[p] == False:
            return int(1e9)

    for o in otherteam:
        osum += people[o]
        if ovisit[o] == False:
            return int(1e9)

    return abs(msum-osum)


def combinations(cnt, maxcnt, select):
    global answer
    if cnt == maxcnt:
        # print(select)
        # print(garimandering(select))
        answer = min(answer, garimandering(select))

    start = lst.index(select[-1])+1 if select else 0
    for i in range(start, len(lst)):
        select.append(lst[i])
        combinations(cnt+1, maxcnt, select)
        select.pop()

def simulate():
    for i in range(1, N):
        combinations(0, i, [])

N = int(input())
people = [0] + list(map(int, input().split()))
lst = [i for i in range(1, N+1)]
graph = dict()
zero_cnt = 0
zero_idx = -1
connect = [[False]*(N+1) for _ in range(N+1)]
answer = int(1e9)
for idx in range(1, N+1):
    data = list(map(int, input().split()))
    if data[0] == 0:
        zero_cnt += 1
        zero_idx = idx
    for d in data[1:]:
        connect[d][idx] = True
        connect[idx][d] = True
    graph[idx] = data[1:]

if zero_cnt > 1 and N > 2:
    print(-1)
elif zero_cnt == 1 and N > 2:
    print(abs(sum(people)-(2*people[zero_idx])))
else:
    simulate()
    if answer == int(1e9):
        print(-1)
    else:
        print(answer)