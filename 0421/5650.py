from collections import defaultdict, deque
# 북 동 남 서
dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]

def simul_crush(row, col, dir):
    if (graph[row][col]==1 and dir == 3) or (graph[row][col]==2 and dir==0) or (graph[row][col]==3 and dir==1) or (graph[row][col]==4 and dir == 2):
        return (row, col, (dir+1)%4)
    elif (graph[row][col]==1 and dir == 2) or (graph[row][col]==2 and dir==3) or (graph[row][col]==3 and dir==0) or (graph[row][col]==4 and dir==1):
        if dir == 0: dir = 4
        return (row, col, (dir-1)%4)
    else:
        return (row, col, (dir+2)%4)

def simul_wormhole(row, col, dir):
    wormhole_num = graph[row][col]
    for pos in wormhole[wormhole_num]:
        if pos != (row, col):
            return (row, col, dir)

def do_simul(sr, sc, sd):
    global answer
    grade = 0
    queue = deque()
    queue.append([sr, sc, sd])
    flag = False
    while queue:
        nr, nc, nd = queue.popleft()
        if (nr, nc) in blackhole:
            answer.append(grade)
            return
        if (nr, nc) == (sr, sc):
            if flag == True:
                answer.append(grade)
                return
            else:
                flag = True

        if graph[nr][nc] in [1,2,3,4,5]:
            mr, mc, md = simul_crush(nr, nc, nd)
            grade += 1
        elif graph[nr][nc] in [6,7,8,9,10]:
            mr, mc, md = simul_wormhole(nr, nc, nd)
        elif (nr == 0 and nd==0) or (nc == 0 and nd==3) or (nr==N-1 and nd==2) or (nc==N-1 and nd==1):
            mr, mc, md = simul_crush(nr, nc, nd)
            grade += 1
        else:
            mr, mc = nr+dr[nd], nc+dc[nd]
            md = nd
        queue.append([mr, mc, md])

def make_start(N):
    for i in range(N):
        for j in range(N):
            for k in range(4):
                if graph[i][j] == 0:
                    do_simul(i, j, k)


T = int(input())

wormhole = defaultdict(list)
blackhole = list()
answer = []

for t in range(T):
    N = int(input())
    graph = []
    for i in range(N):
        data = list(map(int, input().split()))
        for j in range(N):
            if data[j] == -1:
                blackhole.append((i, j))
            elif data[j] in [6,7,8,9,10]:
                wormhole[data[i]].append((i, j))
        graph.append(data)
    make_start(N)

print("A")
print(answer)