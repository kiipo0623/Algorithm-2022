from collections import deque
drow = [0, -1, 0, 1, 0]
dcol = [0, 0, 1, 0, -1]

def bfs(idx, col, row, power):
    global graph
    visited = [[False]*10 for _ in range(10)]

    queue = deque()
    queue.append([row, col, 0])

    while queue:
        brow, bcol, cnt = queue.popleft()
        if visited[brow][bcol] == False:
            graph[brow][bcol].append(idx)
            visited[brow][bcol] = True

        for i in range(1, 5):
            arow, acol = brow+drow[i], bcol+dcol[i]
            if 0<=arow<10 and 0<=acol<10 and cnt+1<=power:
                queue.append([arow, acol, cnt+1])

def check_power(Abattery, Bbattery):
    max_ = 0
    if len(Abattery) == len(Bbattery) == 0:
        return max_
    elif len(Abattery) == 0:
        for b in Bbattery:
            max_ = max(max_, BC[b])
    elif len(Bbattery) == 0:
        for a in Abattery:
            max_ = max(max_, BC[a])
    else:
        for a in Abattery:
            for b in Bbattery:
                if a==b:
                    max_ = max(max_, BC[a])
                else:
                    max_ = max(max_, BC[a]+BC[b])
    return max_

def move_AB():
    grade = 0
    Arow, Acol, Brow, Bcol = 0, 0, 9, 9
    for i in range(M+1):
        Amv, Bmv = userA[i], userB[i]
        Arow += drow[Amv]
        Acol += dcol[Amv]
        Brow += drow[Bmv]
        Bcol += dcol[Bmv]
        Agrade = graph[Arow][Acol]
        Bgrade = graph[Brow][Bcol]
        nowgrade = check_power(Agrade, Bgrade)
        grade += nowgrade
    return grade

# import sys
# sys.stdin = open("sample_input.txt", "r")
T = int(input())
for t in range(T):
    graph = [[[] for _ in range(10)] for _ in range(10)]
    M, A = map(int, input().split())
    userA = [0] + list(map(int, input().split()))
    userB = [0] + list(map(int, input().split()))
    BC = [0]*A
    for i in range(A):
        X, Y, C, P = map(int, input().split())
        bfs(i, X-1, Y-1, C)
        BC[i] = P
    print('#%d %d'%(t+1, move_AB()))