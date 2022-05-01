from collections import deque
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def checkout(row, col):
    if row<0 or row>=N or col<0 or col>=M:
        return True
    return False

def bfs(i, j):
    global visit
    queue = deque([])
    queue.append((i, j))
    ground = []
    ground.append((i, j))
    visit[i][j] = True

    while queue:
        row, col = queue.popleft()
        for k in range(4):
            drow, dcol = row+dx[k], col+dy[k]
            if not checkout(drow, dcol) and not visit[drow][dcol] and board[drow][dcol] == 1:
                visit[drow][dcol] = True
                ground.append((drow, dcol))
                queue.append((drow, dcol))

    return ground


def find_island():
    global island
    for i in range(N):
        for j in range(M):
            if not visit[i][j] and board[i][j] == 1:
                one = bfs(i, j)
                island.append(one)

def check_bridge(r1, r2, c1, c2, rc):
    if rc == 0: #row끼리 같은 경우
        start, end = min(c1, c2), max(c1, c2)
        cnt = 0
        for i in range(start+1, end):
            if board[r1][i] == 1:
                return INF
            cnt += 1
        return cnt if cnt>1 else INF

    elif rc == 1: #col끼리 같은 경우
        start, end = min(r1, r2), max(r1, r2)
        cnt = 0
        for i in range(start+1, end):
            if board[i][c1] == 1:
                return INF
            cnt += 1
        return cnt if cnt>1 else INF


def find_distance(is1, is2):
    is1_pos = island[is1]
    is2_pos = island[is2]
    min_dis = INF
    for r1, c1 in is1_pos:
        for r2, c2 in is2_pos:
            if r1 == r2:
                min_dis = min(min_dis, check_bridge(r1, r2, c1, c2, 0))
            if c1 == c2:
                min_dis = min(min_dis, check_bridge(r1, r2, c1, c2, 1))
    return min_dis

def get_distance():
    for i in range(ISLAND):
        for j in range(ISLAND):
            if i == j:
                continue
            else:
                d = find_distance(i, j)
                distance[i][j] = d
                distance[j][i] = d

def prim():
    select, unselect = [0], [i for i in range(1, ISLAND)]
    # 불가능한 조건
    cannotflag = True
    for i in range(len(distance)):
        if min(distance[i]) != INF:
            cannotflag = False
            break
    if cannotflag == True:
        return -1

    ans = 0
    while len(select)<ISLAND:
        min_, item = INF, INF
        for sidx, s in enumerate(select):
            for uidx, u in enumerate(unselect):
                if distance[s][u] < min_:
                    min_, item = distance[s][u], u
        select.append(item)
        unselect.remove(item)
        ans += min_
    return ans

def simulate():
    global distance, ISLAND
    # 섬 찾기
    find_island()
    # print(island)
    ISLAND = len(island) # 섬의 개수
    # print(ISLAND)
    distance = [[INF]*ISLAND for _ in range(ISLAND)] # 거리 함수
    # 섬 간 다리 최소 길이
    get_distance()
    # print(distance)
    # 연결 최솟값
    ans = prim()
    print(ans)


N, M = map(int, input().split())
board = []
island = []
distance = []
ISLAND = -1
INF = int(1e9)
visit = [[False]*M for _ in range(N)]
for _ in range(N):
    board.append(list(map(int, input().split())))
simulate()
