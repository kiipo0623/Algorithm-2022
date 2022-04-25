from collections import deque
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
INF = int(1e9)
def take_pas(s_row, s_col):
    visited = [[INF] * N for _ in range(N)]
    queue = deque([])
    queue.append([s_row, s_col])
    visited[s_row][s_col] = 0

    while queue:
        n_row, n_col = queue.popleft()
        for i in range(4):
            d_row, d_col = n_row + dx[i], n_col + dy[i]
            if 0 <= d_row < N and 0 <= d_col < N and board[d_row][d_col] == 0 and visited[d_row][d_col] > visited[n_row][n_col]+1:
                visited[d_row][d_col] = visited[n_row][n_col] + 1
                queue.append([d_row, d_col])
    return visited

def bfs(s_row, s_col, e_row, e_col):
    visited = [[-1]*N for _ in range(N)]
    queue = deque([])
    queue.append([s_row, s_col])
    visited[s_row][s_col] = 0

    while queue:
        n_row, n_col = queue.popleft()
        if n_row == e_row and n_col == e_col:
            return visited[n_row][n_col]
        for i in range(4):
            d_row, d_col = n_row+dx[i], n_col+dy[i]
            if 0<=d_row<N and 0<=d_col<N and board[d_row][d_col] == 0 and visited[d_row][d_col] == -1:
                visited[d_row][d_col] = visited[n_row][n_col]+1
                queue.append([d_row, d_col])
    return INF

def simulate2():
    global taxi_row, taxi_col, fuel
    for i in range(M):
        dis = take_pas(taxi_row, taxi_col)
        tmp = []
        for idx in range(len(passenger)):
            pas_x, pas_y, _, _ = passenger[idx]
            tmp.append([dis[pas_x][pas_y], pas_x, pas_y, idx])
        tmp.sort(key=lambda x: (x[0], x[1], x[2]))
        pas_idx = tmp[0][3]
        if tmp[0][0] == INF:
            return -1

        taxi_to_pas = tmp[0][0]
        start_to_end = bfs(passenger[pas_idx][0], passenger[pas_idx][1], passenger[pas_idx][2], passenger[pas_idx][3])

        if taxi_to_pas > fuel:
            return -1
        else:
            fuel -= taxi_to_pas
        # 출발에서 도착까지 감
        if start_to_end > fuel:
            return -1
        else:
            fuel -= start_to_end
            # 연료 갱신
            fuel += (start_to_end) * 2
        # 택시 갱신
        taxi_row, taxi_col = passenger[pas_idx][2], passenger[pas_idx][3]
        # 손님 제거
        del passenger[pas_idx]

    return fuel

def simulate():
    global fuel, taxi_row, taxi_col
    for _ in range(M):
        num = len(passenger)
        topas_distance = [0]*num
        tmp = []
        # 승객과의 거리 구하기
        for i in range(num):
            d = bfs(taxi_row, taxi_col, passenger[i][0], passenger[i][1])
            topas_distance[i] = d

            tmp.append([d, passenger[i][0], passenger[i][1], i])
        # print("topas_dis", topas_distance)

        # 1순위 손님 찾기
        tmp.sort(key = lambda x : (x[0], x[1], x[2]))
        pas_idx = tmp[0][3]
        # print("pas_idx", pas_idx)
        if topas_distance[pas_idx] == INF:
            return -1

        # 이동
        taxi_to_pas = topas_distance[pas_idx]
        start_to_end = bfs(passenger[pas_idx][0], passenger[pas_idx][1], passenger[pas_idx][2], passenger[pas_idx][3])
        # print("taxi to pas", taxi_to_pas)
        # print("start to end", start_to_end)
        # 택시에서 손님까지 감
        if taxi_to_pas > fuel:
            return -1
        else:
            fuel -= taxi_to_pas
        # 출발에서 도착까지 감
        if start_to_end > fuel:
            return -1
        else:
            fuel -= start_to_end
        # 연료 갱신
            fuel += (start_to_end)*2
        # 택시 갱신
        taxi_row, taxi_col = passenger[pas_idx][2], passenger[pas_idx][3]
        # 손님 제거
        del passenger[pas_idx]
        # print("fuel", fuel)
        # print("pas", passenger, len(passenger))
    return fuel

N, M, fuel = map(int, input().split())
board = []
passenger = []
for _ in range(N):
    board.append(list(map(int, input().split())))
taxi_row, taxi_col = map(int, input().split())
taxi_row -= 1
taxi_col -= 1
for _ in range(M):
    data = list(map(int, input().split()))
    data = [i-1 for i in data]
    passenger.append(data)

print(simulate2())
