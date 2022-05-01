from collections import deque

def bfs(start):
    queue = deque([])
    queue.append(start)
    visit = [False]*(N+1)
    visit[0] = True
    visit[start] = True
    while queue:
        now = queue.popleft()
        for city in graph[now]:
            if not city[visit]:
                visit.append(queue)
    return visit

def garimandering(select, v): # 1 2번 포함 :
    if cache[v]:
        return cache

    else: # 캐시 없으면 직접 확인
        myteam = select
        otherteam = [i for i in range(1, N+1) if i not in select]
        mvisit, ovisit = bfs(myteam[0]), bfs(otherteam[0])
        msum, osum = 0, 0
        for p in myteam:
            msum += people[p]
            if mvisit[p] == False:
                return -1

        for o in otherteam:
            osum += people[o]
            if ovisit[p] == False:
                return -1

        return abs(msum-osum)


def combinations(cnt, maxcnt, select, v):
    if cnt == maxcnt:
        garimandering(select, v)

    start = lst.index(select[-1])+1 if select else 0
    for i in range(start, len(lst)):
        select.append(lst[i])
        combinations(cnt+1, maxcnt, v|1<<lst[i], select)
        select.pop()

N = int(input())
people = [0] + list(map(int, input().split()))
lst = [i for i in range(1, N+1)]
graph = dict()
zero_cnt = 0
zero_idx = -1
cache = [None]*((1<<N)-1)
for idx in range(1, N+1):
    data = list(map(int, input().split()))
    if data[0] == 0:
        zero_cnt += 1
        zero_idx = idx
    graph[idx] = data[1:]

if zero_cnt > 1:
    print(-1)
elif zero_cnt == 1:
    print(sum(people)-(2*people[zero_idx]))
# else:
    # simulate()
