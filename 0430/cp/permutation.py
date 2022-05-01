def permutations(cnt, maxcnt, select, visited):
    global perm
    if cnt == maxcnt:
        perm.append(select[:])

    for i in range(len(lst)):
        if not visited[i]:
            select.append(lst[i])
            visited[i] = True
            permutations(cnt+1, maxcnt, select, visited)
            select.pop()
            visited[i] = False

def combinations(cnt, maxcnt, select):
    global comb
    if cnt == maxcnt:
        comb.append(select[:])

    start = lst.index(select[-1])+1 if select else 0
    for i in range(start, len(lst)):
        select.append(lst[i])
        combinations(cnt+1, maxcnt, select)
        select.pop()

def combinations_with_replcement(cnt, maxcnt, select, scounter):
    global c_w_r
    if cnt == maxcnt:
        c_w_r.append(select[:])

    if not select:
        start = 0
    else:
        last = lst.index(select[-1])
        if scounter[last] < maxcnt:
            start = last
        else:
            start = last + 1
    for i in range(start, len(lst)):
        select.append(lst[i])
        scounter[i] += 1
        combinations_with_replcement(cnt+1, maxcnt, select, scounter)
        select.pop()
        scounter[i] -= 1

lst = 'ABCD'
perm = []
comb = []
c_w_r = []
permutations(0, 2, [], [False]*4)
combinations(0, 2, [])
combinations_with_replcement(0, 3, [], [0]*4)
print(perm)
print(comb)
print(c_w_r)